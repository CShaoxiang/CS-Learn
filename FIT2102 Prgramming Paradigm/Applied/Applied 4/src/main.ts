/**
 * Accumulating state and RNG.
 *
 * Please have a look at the README file before attempting these exercises.
 *
 * Notice, when we open the page in the chrome browser, that a circle is
 * drawn to the screen. This is where your visualisation of the Pi
 * approximation process will appear.
 *
 * You need to implement the random number stream and process the numbers
 * to perform the calculation.
 *
 * Please complete the visualisation by drawing dots at the coordinates
 * produced by the random number stream.
 *
 * Points within the circle should be a different colour to those outside
 * the circle.
 *
 * Use the random points from the stream to calculate a Pi approximation,
 * and place the result in the resultInPage element.
 *
 * Refer to the Observable Cheatsheet in Functional Reactive Programming
 * and API Docs for RxJS.
 *
 * There are hints throughout these exercises encoded in base64.
 * You can use online tools such as https://www.base64decode.org/
 * to decode them.
 */

import "./style.css";

import { filter, map, scan, tap } from "rxjs/operators";
import { fromEvent, interval, merge, zip, from, Subscription } from "rxjs";

import type { Observable } from "rxjs";

// Stub value to indicate an implementation
const IMPLEMENT_THIS: any = undefined;
type IMPLEMENT_THIS = any;

/**
 * A random number generator which provides two pure functions
 * `hash` and `scaleToRange`.  Call `hash` repeatedly to generate the
 * sequence of hashes.
 */
abstract class RNG {
    // LCG using GCC's constants
    private static m = 0x80000000; // 2**31
    private static a = 1103515245;
    private static c = 12345;

    /**
     * Call `hash` repeatedly to generate the sequence of hashes.
     * @param seed
     * @returns a hash of the seed
     */
    public static hash = (seed: number) => (RNG.a * seed + RNG.c) % RNG.m;

    /**
     * Takes hash value and scales it to the range [-1, 1]
     */
    public static scale = (hash: number) => (2 * hash) / (RNG.m - 1) - 1;
}

/*****************************************************************
 * Exercise 1
 *
 * Create rng helper functions using the functions in RNG. We at least want a function that
 * creates an observable stream that represents a stream of random
 * numbers. The numbers in the range [-1, 1].
 *
 * /Hint/: An RNG stream will need to accumulate state to produce a stream of random values.
 *
 * /Hint 2/: Use
 *
 * /Challenge/: Implement this using a lazy sequence of random numbers.
 * It is interesting and more generally useful than just a stream.
 * Ask your tutor if you're not sure where to start.
 */

/**
 * Converts values in a stream to random numbers in the range [-1, 1]
 *
 * This usually would be implemented as an RxJS operator, but that is currently
 * beyond the scope of this course.
 *
 * @param source$ The source Observable, elements of this are replaced with random numbers
 * @param seed The seed for the random number generator
 */
export function createRngStreamFromSource<T>(source$: Observable<T>) {
    return function createRngStream(seed: number = 0): Observable<number> {
        const randomNumberStream = source$.pipe(
            scan((current, _) => RNG.hash(current), seed),
            map((scale) => RNG.scale(scale)),
        );

        return randomNumberStream;
    };
}

/*****************************************************************
 * Exercise 2
 *
 * Implement PI Approximation.
 *
 * Make sure to read through the provided code to understand the
 * types and helper functions. This will prevent you from
 * re-implementing something we have already provided.
 *
 */
function piApproximation() {
    /** Custom types */

    /** Colour of dot, green for inside, red for outside */
    type Colour = "red" | "green";

    /** Properties for a dot */
    type Dot = Readonly<{ x: number; y: number; colour: Colour }>;

    /**
     * Test if a point is inside a unit circle
     */
    const inCircle = (x: number, y: number) => x * x + y * y <= 1;

    /** Elements */

    const canvas = document.getElementById("piApproximationVis")!;

    const resultInPage = document.getElementById("value_piApproximation")!;

    /** Constants */

    // Need the circleDiameter to scale the dots to fit the canvas
    // Element.getAttribute is used here as it's called only once at the
    // start of our program, and the canvas size is a fixed value.
    const circleRadius = Number(canvas.getAttribute("width")) / 2;

    /** Helper functions */

    /**
     * Approximate the value of pi using counts
     */
    const approximatePi = (inside: number, total: number) =>
        (4 * inside) / total;

    /**
     * Create a dot on the canvas.
     */
    const addDotToCanvas = (d: Dot) => {
        const dot = document.createElementNS(canvas.namespaceURI, "circle");
        // Set circle properties
        dot.setAttribute("name", "circle");
        dot.setAttribute("cx", String(d.x * circleRadius + circleRadius));
        dot.setAttribute("cy", String(d.y * circleRadius + circleRadius));
        dot.setAttribute("r", "10");
        if (d.colour) dot.setAttribute("fill", d.colour);

        // Add the dot to the canvas
        canvas.appendChild(dot);
    };
    /**
     * Remove all dots from the canvas
     */
    const resetCanvas = () => {
        canvas.querySelectorAll("[name=circle]").forEach((x) => x.remove());
    };

    /** Write your code from here */

    /** State data
     *
     * /Hint/: State We will need to store a count of dots inside the circle and the total number of dots that were created.
     */
    type Data = Readonly<{
        dot?: Dot; // May be initialised without a dot
        counts: number; // Add additional props as you see fit
        total: number;
    }>;

    const rngStream = createRngStreamFromSource(interval(1000));
    const rngStreamY = createRngStreamFromSource(interval(1000));
    const resetButton = document.getElementById("resetButton")!;

    /**
     * /Hint/: We want TWO random values per dot - one for x and one for y
     *
     * /Hint 2/: What state to we need to keep track of (accumulate)?
     *
     * /Hint 3/: Rng streams with a different initial seeds should
     *  produce completely different random values streams
     *
     * /Hint 4/: Observable stream operators What does zip and scan do? 
     * Can we use them to get 2 random values per dot and count the dots that have been generated?
       Make sure to use the Dot type that has been provided!*/

    const dot$ = zip(rngStream(), rngStreamY(1)).pipe(
        scan(
            (acc: Data, [x, y], index: number) => {
                const inside = inCircle(x, y);
                const dot: Dot = {
                    x,
                    y,
                    colour: inside ? "green" : "red",
                };
                console.log(x, y);
                return {
                    dot,
                    counts: acc.counts + (inside ? 1 : 0), // Increment count if inside circle
                    total: index + 1,
                };
            },
            { counts: 0, total: 0 } as Data,
        ),
    );
    const subscription = dot$.subscribe(
        // You may need to destructure more fields here
        ({ dot, counts, total }: Data) => {
            if (dot) {
                addDotToCanvas(dot);
            }
            const piApproximation = approximatePi(counts, total);
            resultInPage.textContent =
                `Approximation: ${piApproximation}` +
                `\ncounts : ${counts}` +
                `\ntotal : ${total}`;
        },
    );

    resetButton.addEventListener("click", () => {
        resetCanvas();
        subscription.unsubscribe();
        piApproximation();
    });
}

/*****************************************************************
 * Exercise 3
 *
 * Reset Button
 *
 * You are required to add a button in to an appropriate location in the HTML
 * This button will need to have the ability to reset the visualisation and approximation
 * This button must not refresh the page, but interact with your observable streams to
 * achieve the appropriate behaviour.
 *
 */

document.addEventListener("DOMContentLoaded", function (event) {
    try {
        piApproximation();
    } catch (e) {
        console.log(e);
    }
});
