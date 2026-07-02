"""Shared style constants for manuscript figure notebooks.

Each figure notebook imports the subset it needs. Putting these constants in
one place keeps the color/marker scheme consistent across every figure.
"""

# Hex colors per tool (matplotlib scatter / line plots).
TOOL_COLORS_HEX = {
    "DCompress":                    "#01B0F0",
    "DCompress (IM)":               "#4571EA",
    "EVo":                          "#E46C0A",
    "MAGEC":                        "#DD94BB",
    "SulfurX":                      "#009E73",
    "VolFe":                        "#FFC00D",
    "VESIcal":                      "#000000",
    "VESIcal_MS":                   "#000000",
    "VESIcal_Dixon":                "#D9D9D9",
    "VESIcal_IaconoMarziano":       "#545454",
    "VESIcal_Iacono":               "#242424",
    "VESIcal_Liu":                  "#532E5C",
    "VESIcal_ShishkinaIdealMixing": "#5E6480",
}

# Marker style per tool for scatter plots.
# Format: (legend_label, marker, size, facecolor, edgecolor, linewidth).
TOOL_MARKER_STYLE_w_HC_MODEL = {
    "DCompress":         ("D-C",              "o", 150, "#01B0F0", "k", 0.5),
    "DCompress (IM)":    ("D-C (IM)",         "s", 150, "#4571EA", "k", 0.5),
    "EVo":               ("EVo (D-C)",        "o", 150, "#E46C0A", "k", 0.5),
    "MAGEC":             ("MAGEC (IM)",       "s", 150, "#DD94BB", "k", 0.5),
    "SulfurX":           ("Sulfur_X (IM*)",   "s", 150, "#009E73", "k", 0.5),
    "VolFe":             ("VolFe (Hughes24)", "^", 150, "#FFC00D", "k", 0.5),
    "VESIcal_Iacono":    ("VESIcal (IM*)",    "s", 120, "#FFFFFF", "k", 1.0),
    "VESIcal_Dixon":     ("VESIcal (VC*)",    "x", 100, "k",         "k", 1.5),
    "VESIcal_MS":        ("VESIcal (MS*)",    "*", 140, "k",         "k", 0.5),
}

TOOL_MARKER_STYLE = {
    "DCompress":       ("D-C",              "o", 150, "#01B0F0", "k", 0.5),
    "DCompress (IM)":  ("D-C (IM)",         "s", 150, "#4571EA", "k", 0.5),
    "EVo":             ("EVo",              "o", 150, "#E46C0A", "k", 0.5),
    "MAGEC":           ("MAGEC",            "s", 150, "#DD94BB", "k", 0.5),
    "SulfurX":         ("Sulfur_X",         "s", 150, "#009E73", "k", 0.5),
    "VolFe":           ("VolFe",            "^", 150, "#FFC00D", "k", 0.5),
    "VESIcal_Iacono":  ("VESIcal (IM)",     "s", 120, "#FFFFFF",      "k", 1.0),
    "VESIcal_Dixon":   ("VESIcal (VC)",     "x", 100, "k",         "k", 1.5),
    "VESIcal_MS":      ("VESIcal (MS)",     "*", 140, "k",         "k", 0.5),
}

TOOL_LINE_STYLE = {
    "DCompress":      "solid",
    "DCompress (IM)": "dash",
    "EVo":            "solid",
    "MAGEC":          "solid",
    "SulfurX":        "solid",
    "VolFe":          "solid",
    "VESIcal_Iacono": "solid",
}

# Presentation-only renames for sample labels (e.g. diacritics).
SAMPLE_DISPLAY_NAMES = {
    "Kilauea": "K\u012blauea",   # Kīlauea
}

# Per-system (volcano) colors for envelope / composition plots.
SYSTEM_COLORS = {
    "MORB":    "#5a80a6",
    "Kilauea": "#f05f70",
    "Fuego":   "#bbbbba",
    "Fogo":    "#9dce58",
}


# ---------------------------------------------------------------------------
# Typography — shared across every figure.
# ---------------------------------------------------------------------------
# Scalar constants; pass them explicitly so it's obvious in each notebook
# which text element is being styled.
AXIS_LABEL_FONTSIZE   = 15   # ax.set_xlabel / set_ylabel
TICK_FONTSIZE         = 12   # ax.tick_params(labelsize=...)
LEGEND_FONTSIZE       = 13   # default legend text
PANEL_TITLE_FONTSIZE  = 20   # in-plot sample labels (e.g. "MORB" over a panel)
ANNOTATION_FONTSIZE   = 12   # small italic notes (e.g. "*EVo > 10,000 bars")


# ---------------------------------------------------------------------------
# Legend style — spread into every ax.legend() call.
# ---------------------------------------------------------------------------
# Usage:  ax.legend(**LEGEND_STYLE, bbox_to_anchor=(...), ncol=2, loc=...)
# ``ncol`` and placement stay figure-specific; the visual frame/fill doesn't.
LEGEND_STYLE = {
    "fontsize":   LEGEND_FONTSIZE,
    "frameon":    True,
    "edgecolor":  "k",
    "facecolor":  "white",
    "framealpha": 1.0,
}


# ---------------------------------------------------------------------------
# Plotly equivalents (Figures 4, 6, 8A).
# ---------------------------------------------------------------------------
# Plotly sizes aren't 1:1 with matplotlib because Plotly ships in a larger
# pixel canvas; the legend size is tuned down to match visual weight.
PLOTLY_FONT = dict(family="Helvetica", color="black")
PLOTLY_AXIS_LABEL_FONTSIZE = 15
PLOTLY_TICK_FONTSIZE       = 12
PLOTLY_LEGEND_FONTSIZE     = 10
PLOTLY_TICK_LEN            = 4


# ---------------------------------------------------------------------------
# Figure save defaults.
# ---------------------------------------------------------------------------
SAVE_DPI = 300
