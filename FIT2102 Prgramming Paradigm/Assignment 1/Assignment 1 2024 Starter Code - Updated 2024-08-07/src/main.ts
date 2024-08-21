/**
 * Inside this file you will use the classes and functions from rx.js
 * to add visuals to the svg element in index.html, animate them, and make them interactive.
 *
 * Study and complete the tasks in observable exercises first to get ideas.
 *
 * Course Notes showing Asteroids in FRP: https://tgdwyer.github.io/asteroids/
 *
 * You will be marked on your functional programming style
 * as well as the functionality that you implement.
 *
 * Document your code!
 */

import "./style.css";

import { fromEvent, interval, merge, Observable } from "rxjs";
import { map, filter, scan } from "rxjs/operators";
import * as Tone from "tone";
import { SampleLibrary } from "./tonejs-instruments";
import { State, initialState } from "./state";
import { Constants, Viewport, Note, Key, Event } from "./types";
import { updateView } from "./view";
import {playInstrument,RNG} from './util'
import { AnyCatcher } from "rxjs/internal/AnyCatcher";

/**
 * This is the function called on page load. Your main game loop
 * should be called here.
 */
export function main(
    csvContents: string,
    samples: { [key: string]: Tone.Sampler },
) {

    /** User input */

const key$ = (e: Event , k : Key) => fromEvent<KeyboardEvent>(document,e)
        .pipe(
            filter(({code}) => code === k)),

        playInColumn1$ = key$('keydown','KeyH'),
        playInColumn2$ = key$('keydown','KeyJ'),
        playInColumn3$ = key$('keydown', 'KeyK'),
        playInColumn4$ = key$('keydown','KeyL'),

        rng$ = (source : Observable<any>) => (seed : number) => source.pipe(
            scan(a => RNG.hash(a),seed),
            map(RNG.scale),
        )
       


    

    /** Determines the rate of time steps */
    const tick$ = interval(Constants.TICK_RATE_MS);

    /**
     * Renders the current state to the canvas.
     *
     * In MVC terms, this updates the View using the Model.
     *
     * @param s Current state
     */

    const source$ = tick$
        .pipe(
            scan(
                (s: State) => ({
                    circles: [],
                    score: 0,
                    multiplier: 1,
                    gameEnd: false,
                }),
                initialState,
            ),
        )
        .subscribe((s: State) => {
            updateView();
        });
}

// The following simply runs your main function on window load.  Make sure to leave it in place.
// You should not need to change this, beware if you are.
if (typeof window !== "undefined") {
    // Load in the instruments and then start your game!
    const samples = SampleLibrary.load({
        instruments: [
            "bass-electric",
            "violin",
            "piano",
            "trumpet",
            "saxophone",
            "trombone",
            "flute",
        ], // SampleLibrary.list,
        baseUrl: "samples/",
    });

    const startGame = (contents: string) => {
        document.body.addEventListener(
            "mousedown",
            function () {
                main(contents, samples);
            },
            { once: true },
        );
    };

    const { protocol, hostname, port } = new URL(import.meta.url);
    const baseUrl = `${protocol}//${hostname}${port ? `:${port}` : ""}`;

    Tone.ToneAudioBuffer.loaded().then(() => {
        for (const instrument in samples) {
            samples[instrument].toDestination();
            samples[instrument].release = 0.5;
        }

        fetch(`${baseUrl}/assets/${Constants.SONG_NAME}.csv`)
            .then((response) => response.text())
            .then((text) => startGame(text))
            .catch((error) =>
                console.error("Error fetching the CSV file:", error),
            );
    });
}
