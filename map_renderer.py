"""Map renderer - draws T map pixels on the LED matrix canvas."""
from map_data import PIXELS, STATIONS, COLORS, COLORS_DIM

# Dark grey for "off" LEDs (background)
OFF_COLOR = (20, 20, 20)


def draw_map(canvas):
    """Draw all T line pixels on the canvas.
    
    Background is dark grey to simulate off LEDs.
    Stations are full brightness, track between is dimmed.
    """
    # Fill entire canvas with dark grey (off LEDs)
    for y in range(64):
        for x in range(64):
            canvas.SetPixel(x, y, *OFF_COLOR)
    
    # Draw the track lines on top
    for line_name, coords in PIXELS.items():
        station_set = set(STATIONS.get(line_name, []))
        full_color = COLORS[line_name]
        dim_color = COLORS_DIM[line_name]
        
        for x, y in coords:
            if (x, y) in station_set:
                r, g, b = full_color
            else:
                r, g, b = dim_color
            canvas.SetPixel(x, y, r, g, b)
