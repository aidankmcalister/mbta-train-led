"""Boston T Map LED Matrix Display - Real-time train visualization."""
import time
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
from map_renderer import draw_map


def main():
    # Configure 64x64 matrix
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64

    matrix = RGBMatrix(options=options)
    canvas = matrix.CreateFrameCanvas()

    while True:
        canvas.Clear()
        draw_map(canvas)
        matrix.SwapOnVSync(canvas)
        time.sleep(0.1)


if __name__ == "__main__":
    print("Boston T Map - Starting...")
    main()
