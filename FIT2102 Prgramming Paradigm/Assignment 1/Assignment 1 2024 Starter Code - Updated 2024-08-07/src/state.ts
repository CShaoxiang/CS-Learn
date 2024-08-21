export type { State };
export { initialState, tick };

import { State, Note } from "./types";

/** State processing */

/**
 * Updates the state by proceeding with one time step.
 *
 * @param s Current state
 * @returns Updated state
 */
const tick = (s: State) => s;

const initialState: State = {
    circles: [],
    score: 0,
    multiplier: 1,
    gameEnd: false,
} as const;
