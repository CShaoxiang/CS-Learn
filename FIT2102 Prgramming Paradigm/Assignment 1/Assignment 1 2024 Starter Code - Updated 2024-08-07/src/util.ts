import { Note, Constants } from "./types";
import * as Tone from "tone";
import { SampleLibrary } from "./tonejs-instruments";

export {playInstrument, RNG}
/** Utility functions */
/* This function converts the the CSV file content from strings -> Readonly<NoteI>[] */
function extractNote(csvContents: string) {
    const line = csvContents.split("\n");

    const notes: Note[] = line
        .filter((line) => line.trim() !== "")
        .map((line) => {
            const [userPlayed, instrumentName, velocity, pitch, start, end] =
                line.split(",");
            return {
                userPlayed: userPlayed === "True", // Convert userPlayed to a boolean
                instrumentName,
                velocity: parseInt(velocity, 10),  //base 10
                pitch: parseInt(pitch, 10),
                length: parseFloat(end) - parseFloat(start),  // calculates the time of the note 
            } as Note;
        });
    return notes;
}


const samples = SampleLibrary.load({
    instruments: SampleLibrary.list,
    baseUrl: "samples/",
});

Tone.ToneAudioBuffer.loaded().then(() => {
    for (const instrument in samples) {
        samples[instrument].toDestination();
        samples[instrument].release = 0.5;
    }
    playInstrument();
});

function playInstrument(note : Note) {

            samples[`${note.instrumentName}`].triggerAttackRelease(
            Tone.Frequency(note.pitch, "midi").toNote(), // Convert MIDI note to frequency
            note.length, // Duration of the note in seconds
            undefined, // Use default time for note onset
            note.velocity, // Set velocity to quarter of the maximum velocity
        );
}




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
 h    * Takes hash value and scales it to the range [-1, 1]
     */
    public static scale = (hash: number) => (2 * hash) / (RNG.m - 1) - 1;
}