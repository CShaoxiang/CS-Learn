export { Constants, Viewport, NoteSize };
export type { Key, Event, State, Note };

/** Constants */

const Viewport = {
    CANVAS_WIDTH: 200,
    CANVAS_HEIGHT: 400,
} as const;

const Constants = {
    TICK_RATE_MS: 500,
    SONG_NAME: "RockinRobin",
} as const;

const NoteSize = {
    RADIUS: 0.07 * Viewport.CANVAS_WIDTH,
    TAIL_WIDTH: 10,
};

interface NoteI {
    userPlayed: boolean;
    instrumentName: string;
    velocity: number;
    pitch: number;
    length: number;
}

type Note = Readonly<NoteI>;
/** User input */

type Key = "KeyH" | "KeyJ" | "KeyK" | "KeyL";

type Event = "keydown" | "keyup" | "keypress";

/** Game State */
interface IState {
    circles: ReadonlyArray<NoteI>;
    score: number;
    multiplier: 1;
    gameEnd: boolean;
}
type State = Readonly<IState>;
