import { fromEvent, merge, Observable, timer, from } from "rxjs";
import { flatMap, map, mergeMap, startWith, take } from "rxjs/operators";
import * as Tone from "tone";
import { SampleLibrary } from "./tonejs-instruments";

function pianoKeyToMidi(key: string): number {
    const whiteKeyBase = 60; // MIDI note for C4
    const blackKeyOffsets = [1, 3, 6, 8, 10];
    const whiteKeyOffsets = [0, 2, 4, 5, 7, 9, 11];

    // Check if the key is white or black
    if (key.startsWith("w")) {
        const keyNumber = parseInt(key.substring(1), 10);
        const octaveShift = Math.floor((keyNumber - 1) / 7) * 12;
        const offsetIndex = (keyNumber - 1) % 7;
        return whiteKeyBase + whiteKeyOffsets[offsetIndex] + octaveShift;
    } else if (key.startsWith("b")) {
        const keyNumber = parseInt(key.substring(1), 10);
        const octaveShift = Math.floor((keyNumber - 1) / 5) * 12;
        const offsetIndex = (keyNumber - 1) % 5;
        return whiteKeyBase + blackKeyOffsets[offsetIndex] + octaveShift;
    } else {
        throw new Error("Invalid key identifier");
    }
}

const samples = SampleLibrary.load({
    instruments: ["piano"],
    baseUrl: "samples/",
});

const IMPLEMENT_THIS: any = undefined;
type IMPLEMENT_THIS = any;

/*****************************************************************
 * Exercise 4
 * For each ID in the provided array of IDs,
 * return the corresponding HTML element using document.getElementById.
 *
 * Do *not* use the ! operator to handle nulls.
 * Do *not* use the filter, operation, but play around with flatMap.
 *
 * /Hint/: flatMap will be the function to use
 */

export function getAllElements(): readonly HTMLElement[] {
    const range = (n: number) => [...Array(n)].map((_, idx) => idx);

    const bRange = range(11)
        .map((x) => x + 1)
        .map((x) => `b${x}`);
    const wRange = range(16)
        .map((x) => x + 1)
        .map((x) => `w${x}`);

    // Element IDs of all black and white keys
    const allIds = bRange.concat(wRange);

    return allIds.flatMap((key) => {
        const element = document.getElementById(key);
        return element ? [element] : [];
    });
}

/*****************************************************************
 * Exercise 5
 * This function merges the streams of mousedown and mouseup events for a given HTML element.
 * The mouseup event is not guaranteed to be triggered on the same element where the mousedown is triggered.
 * Your aim is to create a stream of both mouseup and mousedown events for a given element,
 * where the mouseup event will be associated with the element where the mousedown occurred.
 *
 * 1. Create an observable stream of mousedown events on the given element.
 *    - Use the `fromEvent` function to create the stream.
 *    - Use `mergeMap` to listen for mouseup events after each mousedown event on the element.
 *    - /Hint/: You may need to use `startWith`.
 *    - /Hint/: Ensure `mouseup` is only fired once.
 *
 * 2. Return the merged stream.
 *
 * The merged stream will emit an object indicating whether the mouse is down (start: true) or up (start: false),
 *       along with the element that triggered the mousedown event.
 *
 *****************************************************************/

type MouseUpDownEvent = Readonly<{
    start: boolean;
    element: HTMLElement;
}>;

export function mergeUpDown(
    element: HTMLElement,
): Observable<MouseUpDownEvent> {
    const mousedown$ = fromEvent<MouseEvent>(element, "mousedown").pipe(
        map((): MouseUpDownEvent => ({ start: true, element: element })),
    );

    const mouseup$ = mousedown$.pipe(
        mergeMap(() =>
            fromEvent<MouseEvent>(document, "mouseup").pipe(
                take(1),
                map(
                    (): MouseUpDownEvent => ({
                        start: false,
                        element: element,
                    }),
                ),
            ),
        ),
    );

    return merge(mousedown$, mouseup$);
}

/*****************************************************************
 * This function sets up a stream of mouse events for the piano keys,
 * highlighting them on mousedown and removing the highlight on mouseup.
 * Additionally, it triggers the appropriate piano note when an element is clicked.
 *
 * You will need to use the two previous functions to:
 * - find all piano keys
 * - create a stream of mousedown/mouseup.
 *
 * There is nothing to do for the `example` function, but is here to show how you can both
 * play a note and add a highlight to the note
 * Feel free to delete this when you have your main function completed.
 */

function example() {
    const element = document.getElementById("b1")!;

    // Adding the `highlight` class to make the key highlighted.
    // You can use the `remove` function to remove the highlight.
    element.classList.add("highlight");
    const note = Tone.Frequency(pianoKeyToMidi(element.id), "midi").toNote(); // Convert MIDI note to frequency

    // Start the note
    samples["piano"].triggerAttack(
        note,
        undefined, // Use default time for note onset
        0.8, // Set velocity to 80% the max
    );

    // Release the note
    timer(1000).subscribe((_) => {
        samples["piano"].triggerRelease(note);
    });
}

/*****************************************************************
 * Exercise 6
 * This function enhances the interactivity of piano keys by responding to mouse events.
 * It visually highlights the keys when pressed and triggers corresponding piano notes.
 *
 * Overview:
 *
 * - Subscribe to the stream to listen for events.
 * - When a key is pressed (mousedown):
 *   - Highlight the key to provide visual feedback.
 *   - Convert the key identifier to a musical note and trigger the corresponding sound.
 * - When the key is released (mouseup):
 *   - Remove the highlight from the key.
 *   - Stop the sound associated with the key.
 *
 *****************************************************************/

function main() {
    const keyElements = getAllElements(); // Get all piano key elements

    keyElements.forEach((keyElement) => {
        const keyId = keyElement.id;

        // Subscribe to mousedown and mouseup events
        mergeUpDown(keyElement).subscribe((event) => {
            if (event.start) {
                keyElement.classList.add("highlight"); // Add visual feedback (highlight the key)

                const note = Tone.Frequency(
                    pianoKeyToMidi(keyId),
                    "midi",
                ).toNote();
                const instrument = samples["piano"];
                instrument.triggerAttack(note, undefined, 1.5);
            } else {
                // mouse up
                keyElement.classList.remove("highlight");

                const midiNote = pianoKeyToMidi(keyId);
                const instrument = samples["piano"];
                instrument.triggerRelease(midiNote);
            }
        });
    });
}

export const run = () => {
    Tone.ToneAudioBuffer.loaded().then(() => {
        for (const instrument in samples) {
            samples[instrument].toDestination();
            samples[instrument].release = 0.5;
        }
        main();
    });
};
