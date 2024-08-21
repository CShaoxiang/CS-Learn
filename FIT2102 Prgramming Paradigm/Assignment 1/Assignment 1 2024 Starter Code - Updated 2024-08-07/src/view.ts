export { updateView };

import { Viewport, State, NoteSize } from "./types";

/** Rendering (side effects) */
/**
 * Creates an SVG element with the given properties.
 *
 * See https://developer.mozilla.org/en-US/docs/Web/SVG/Element for valid
 * element names and properties.
 *
 * @param namespace Namespace of the SVG element
 * @param name SVGElement name
 * @param props Properties to set on the SVG element
 * @returns SVG element
 */

function updateView(onFinish: () => void) {
    return function (s: State): void {
        // Canvas elements
        const svg = document.querySelector("#svgCanvas") as SVGGraphicsElement &
            HTMLElement;
        const preview = document.querySelector(
            "#svgPreview",
        ) as SVGGraphicsElement & HTMLElement;
        const gameover = document.querySelector(
            "#gameOver",
        ) as SVGGraphicsElement & HTMLElement;
        const container = document.querySelector("#main") as HTMLElement;

        svg.setAttribute("height", `${Viewport.CANVAS_HEIGHT}`);
        svg.setAttribute("width", `${Viewport.CANVAS_WIDTH}`);

        // Text fields
        const multiplier = document.querySelector(
            "#multiplierText",
        ) as HTMLElement;
        const scoreText = document.querySelector("#scoreText") as HTMLElement;
        const highScoreText = document.querySelector(
            "#highScoreText",
        ) as HTMLElement;

        const render = (s: State) => {
            // Add blocks to the main grid canvas
            const greenCircle = createSvgElement(svg.namespaceURI, "circle", {
                r: `${NoteSize.RADIUS}`,
                cx: "20%",
                cy: "200",
                style: "fill: green",
                class: "shadow",
            });

            const redCircle = createSvgElement(svg.namespaceURI, "circle", {
                r: `${NoteSize.RADIUS}`,
                cx: "40%",
                cy: "50",
                style: "fill: red",
                class: "shadow",
            });

            const blueCircle = createSvgElement(svg.namespaceURI, "circle", {
                r: `${NoteSize.RADIUS}`,
                cx: "60%",
                cy: "50",
                style: "fill: blue",
                class: "shadow",
            });

            const yellowCircle = createSvgElement(svg.namespaceURI, "circle", {
                r: `${NoteSize.RADIUS}`,
                cx: "80%",
                cy: "50",
                style: "fill: yellow",
                class: "shadow",
            });

            svg.appendChild(greenCircle);
            svg.appendChild(redCircle);
            svg.appendChild(blueCircle);
            svg.appendChild(yellowCircle);
        };

        if (s.gameEnd) {
            show(gameover);
        } else {
            hide(gameover);
        }
    };
}

const createSvgElement = (
    namespace: string | null,
    name: string,
    props: Record<string, string> = {},
) => {
    const elem = document.createElementNS(namespace, name) as SVGElement;
    Object.entries(props).forEach(([k, v]) => elem.setAttribute(k, v));
    return elem;
};

/**
 * Displays a SVG element on the canvas. Brings to foreground.
 * @param elem SVG element to display
 */
const show = (elem: SVGGraphicsElement) => {
    elem.setAttribute("visibility", "visible");
    elem.parentNode!.appendChild(elem);
};

/**
 * Hides a SVG element on the canvas.
 * @param elem SVG element to hide
 */
const hide = (elem: SVGGraphicsElement) =>
    elem.setAttribute("visibility", "hidden");
