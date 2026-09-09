"""Canonical, rectangular UTF-8 TSV exports (legacy .csv filenames).

No header row: the explicit schema is returned alongside each matrix.
HTML owns the values; merged cells are repeated, never inferred from CSV.
This module describes/validates data and does not write the library.
"""
import re
from pathlib import Path
from thread_html import Extractor, expand

def rows_from(path, width, pattern):
    parser = Extractor()
    parser.feed(path.read_text(encoding="utf-8-sig"))
    return [
        [c["text"] for c in row]
        for table in parser.tables for row in expand(table)
        if len(row) == width and re.match(pattern, row[0]["text"])
    ]

def export_spec(path):
    """Return the original column order, complete records and source paths."""
    name = path.as_posix()
    sources = [path.with_name("index_cs.html")]
    if "pro vseobecne pouziti/" in name:
        base = path.parents[2]
        sources = sorted(base.glob("0[1-5]-*/0000-index/index_cs.html"))
        if path.name.startswith("table"):
            page = int(path.stem[-1])
            sources = [p for p in sources if p.parent.parent.name.startswith(f"0{page}-")]
        rows = [r for p in sources for r in rows_from(p, 5, r"^M\s*\d")]
        columns = ["designation", "P_mm", "D1_mm", "D2_mm", "d3_mm"]
        if path.name == "tabulka.csv":
            rows = [[re.match(r"^M\s*([\d,.]+)", r[0])[1], r[1], r[3], r[2], r[4], r[0]] for r in rows]
            columns = ["d_mm", "P_mm", "D2_mm", "D1_mm", "d3_mm", "designation"]
    elif "pro jemnou mechaniku" in name:
        rows = rows_from(sources[0], 6, r"^[\d,.]+$")
        columns = ["nominal_mm", "P_mm", "d_mm", "D2_mm", "D1_mm", "d3_mm"]
    elif "02-Palcove zavity ISO - zakladni rozmery" in name:
        rows = rows_from(sources[0], 9, r"^(?:No\.|\d)")
        columns = ["nominal_in", "series", "threads_per_in", "P_mm", "d_in", "d_mm", "D2_in", "D1_in", "designation"]
    elif "04-Whitworthovy" in name:
        rows = rows_from(sources[0], 13, r"^W ")
        columns = ["designation", "threads_per_in", "P_mm", "d_mm", "d_deviations_um", "d2_mm",
                   "d2_deviations_um", "d1_mm", "D_mm", "D2_mm", "D2_deviations_um", "D1_mm", "D1_deviations_um"]
    elif "ISO 7 pro" in name:
        rows = rows_from(sources[0], 11, r"^[\d/ ]+$")
        columns = ["designation", "threads_per_in", "P_mm", "d_mm", "d2_mm", "d1_mm",
                   "gauge_length_max_min_mm", "gauge_length_tolerance_turns", "internal_gauge_plane_tolerance_turns",
                   "external_usable_length_max_min_mm", "assembly_allowance_turns"]
    elif "ISO 228" in name:
        rows = [[r[i] for i in (0, 3, 4, 5)] for r in rows_from(sources[0], 11, r"^G")]
        columns = ["designation", "d_mm", "D2_mm", "D1_mm"]
    elif "01-Lichobeznikove zavity" in name:
        rows = rows_from(sources[0], 14, r"^[\d,.()\s]+$")
        # Blank geometry in the source is intentional; the merged explanatory
        # sentence is prose, not a diameter. No dimensions are invented.
        rows = [[v if j < 3 or j > 6 or re.fullmatch(r"[\d,.]+", v) else "" for j, v in enumerate(r)] for r in rows]
        columns = ["nominal_mm", "P_mm", "d_mm", "D4_mm", "D2_mm", "d3_mm", "D1_mm", "designation"] + [f"Ph_{n}_starts_mm" for n in (1, 2, 3, 4, 6, 8)]
    elif "07-Zvlastni" in name:
        rows = [r[:6] for r in rows_from(sources[0], 7, r"^[*]?\d.*[×x]")]
        columns = ["designation", "threads_per_in", "P_mm", "d_mm", "d2_mm", "d1_mm"]
    elif "08-Vybehy" in name:
        rows = rows_from(sources[0], 11, r"^[\d,.]+$")
        columns = ["P_mm", "coarse_threads", "x_normal_max_mm", "x_short_max_mm", "v_normal_max_mm", "u_normal_min_mm",
                   "v_short_max_mm", "u_short_min_mm", "v_long_max_mm", "u_long_min_mm", "z_min_mm"]
    elif "09-Drazky" in name:
        rows = rows_from(sources[0], 12, r"^[\d,.]+$")
        columns = ["P_mm", "coarse_threads", "dd_mm", "a_min_mm", "b_max_mm", "Dd_mm", "A_normal_max_mm", "B_normal_min_mm",
                   "A_short_max_mm", "B_short_min_mm", "R_external_mm", "R_internal_mm"]
    else:
        raise ValueError(f"Unknown export: {path}")
    if not rows or any(len(r) != len(columns) for r in rows):
        raise ValueError(f"Empty/nonrectangular source: {path}")
    return {"path": path, "sources": sources, "columns": columns, "rows": rows}
