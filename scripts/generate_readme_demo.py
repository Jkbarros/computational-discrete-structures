"""Generate docs/demo.gif — relation vs graph highlight for README."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "demo.gif"
W, H = 720, 200


def font(size: int):
    for name in ("segoeui.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_matrix(draw, ox, oy, cell, active=None):
    for i in range(4):
        for j in range(4):
            x, y = ox + j * cell, oy + i * cell
            val = 1 if (i == j or (i, j) in ((0, 1), (1, 0), (2, 3))) else 0
            fill = (56, 189, 248) if active == (i, j) else ((30, 41, 59) if val else (15, 23, 42))
            draw.rectangle((x, y, x + cell - 2, y + cell - 2), fill=fill, outline=(71, 85, 105))


def draw_graph(draw, ox, oy, highlight_edge=None):
    pts = [(ox + 40, oy + 80), (ox + 120, oy + 30), (ox + 200, oy + 80), (ox + 120, oy + 130)]
    edges = [(0, 1, 3), (1, 2, 7), (2, 3, 6), (3, 0, 5)]
    for a, b, w in edges:
        col = (56, 189, 248) if highlight_edge == (a, b) else (100, 116, 139)
        draw.line((pts[a][0], pts[a][1], pts[b][0], pts[b][1]), fill=col, width=3)
        mx, my = (pts[a][0] + pts[b][0]) // 2, (pts[a][1] + pts[b][1]) // 2
        draw.text((mx, my - 8), str(w), fill=(226, 232, 240), font=font(11))
    for i, (x, y) in enumerate(pts):
        draw.ellipse((x - 14, y - 14, x + 14, y + 14), fill=(30, 41, 59), outline=(148, 163, 184))
        draw.text((x - 4, y - 8), str(i), fill=(226, 232, 240), font=font(12))


def frame(step: int) -> Image.Image:
    img = Image.new("RGB", (W, H), (18, 22, 32))
    d = ImageDraw.Draw(img)
    d.text((24, 16), "COSC 314 — Relations & shortest paths", fill=(226, 232, 240), font=font(20))
    d.text((24, 52), "Project 1: matrix properties", fill=(148, 163, 184), font=font(13))
    active = [(0, 0), (0, 1), (1, 0), (2, 2)][step % 4]
    draw_matrix(d, 24, 78, 22, active=active)
    d.text((280, 52), "Project 2: Dijkstra on a graph", fill=(148, 163, 184), font=font(13))
    edge = [(0, 1), (1, 2), (2, 3), (3, 0)][step % 4]
    draw_graph(d, 300, 58, highlight_edge=edge)
    return img


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames = [frame(i) for i in range(4)]
    frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=850, loop=0, optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
