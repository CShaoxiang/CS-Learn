import { Observable, from, interval, take, zip, Subject } from "rxjs";
import { map, takeUntil, toArray } from "rxjs/operators";
import { createRngStreamFromSource } from "../src/main.ts";
import { getAllElements, mergeUpDown } from "../src/piano.ts";

import { expect } from "chai";

describe("exercise_1_suite", function () {
    describe("createRngStreamFromSource", function () {
        it("is a curried function", function () {
            expect(createRngStreamFromSource).is.a("function");
            expect(createRngStreamFromSource(interval())).is.a("function");
        });
    });

    describe("createRngStream", function () {
        it("creates an Observable stream", function () {
            const createRngStream = createRngStreamFromSource(interval());

            expect(createRngStream).to.not.throw();
            expect(createRngStream()).to.be.an.instanceof(Observable);
        });

        it("returns a stream with values in the range [-1, 1]", function (done) {
            const inf = {
                [Symbol.iterator]: function* () {
                    while (true) yield true;
                },
            };
            const infiniteStream = from(inf);

            const createRngStream = createRngStreamFromSource(infiniteStream);
            createRngStream()
                .pipe(
                    take(500),
                    map((x) => {
                        if (typeof x !== "number") {
                            throw new Error(`Expected ${x} to be a number`);
                        }
                        if (x < -1 || x > 1) {
                            throw new Error(
                                `Expected ${x} to be in range [-1, 1]`,
                            );
                        }
                        return x;
                    }),
                )
                .subscribe({
                    error: expect.fail,
                    complete: done,
                });
        });

        /** Regression test */
        it("returns a stream with with correct values", function (done) {
            const inf = {
                [Symbol.iterator]: function* () {
                    while (true) yield true;
                },
            };
            const infiniteStream = from(inf);

            const createRngStream = createRngStreamFromSource(infiniteStream);
            const sequence = [
                0.16461517995438313, 0.039637327678332834, 0.8298795231757126,
                0.397431135828342, 0.5061624057153997,
            ] as const;

            zip(
                // Prevents infinite stream zipping
                createRngStream(42).pipe(take(sequence.length)),
                // Zips with index
                from(sequence),
            )
                .pipe(
                    map(([x, v]) => {
                        if (x.toFixed(3) !== v.toFixed(3)) {
                            throw new Error(`Expected ${x} to equal ${v}`);
                        }
                        return x;
                    }),
                )
                .subscribe({
                    error: expect.fail,
                    complete: done,
                });
        });
    });
});

describe("exercise_4_suite", function () {
    describe("getAllElements", function () {
        it("is a function", function () {
            expect(getAllElements).is.a("function");
        });
        it("returns correct number of elements", function () {
            expect(getAllElements().length).equal(27);
        });
        it("all elements are HTMLElements", function () {
            getAllElements().forEach((element) => {
                expect(element instanceof HTMLElement).to.be.true;
            });
        });
        it("all elements are unique", function () {
            expect(
                [...new Set(getAllElements().map((x) => x.id))].length,
            ).equal(27);
        });
    });
});

describe("exercise_5_suite", function () {
    describe("mergeUpDown", function () {
        it("is a function", function () {
            expect(mergeUpDown).is.a("function");
        });
        it("simulated user interaction", function (done) {
            const newElement = document.createElement("div");
            newElement.id = "newEle";
            const stop$ = new Subject();
            const obs = mergeUpDown(newElement).pipe(
                takeUntil(stop$),
                toArray(),
            );
            obs.subscribe({
                next: (arr) => {
                    expect(arr.length).eq(2);
                    expect(arr[0].start).to.be.true;
                    expect(arr[1].start).to.be.false;
                    expect(arr[0].element.id).equal("newEle");
                    expect(arr[1].element.id).equal("newEle");
                    done();
                },
                error: expect.fail,
            });
            document.body.appendChild(newElement);

            // Simulate mouse click
            const mouseDownEvent = new MouseEvent("mousedown", {
                view: window,
                bubbles: true,
                cancelable: true,
                clientX: 100,
                clientY: 100,
            });
            newElement.dispatchEvent(mouseDownEvent);

            // Simulate mouse move
            const mouseMoveEvent = new MouseEvent("mousemove", {
                view: window,
                bubbles: true,
                cancelable: true,
                clientX: 150,
                clientY: 150,
            });
            document.dispatchEvent(mouseMoveEvent);

            // Simulate mouse release
            const mouseUpEvent = new MouseEvent("mouseup", {
                view: window,
                bubbles: true,
                cancelable: true,
                clientX: 150,
                clientY: 150,
            });
            document.dispatchEvent(mouseUpEvent);

            document.body.removeChild(newElement);
            stop$.next(0); // Signal completion
            stop$.complete(); // Signal completion
        });
    });
});
