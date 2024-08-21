import { Note, Constants } from "./types";

/** Utility functions */

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
                velocity: parseInt(velocity, 10),
                pitch: parseInt(pitch, 10),
                length: parseFloat(end) - parseFloat(start),
            } as Note;
        });
    return notes;
}
