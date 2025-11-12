"""Gradio application that visualises library seat availability."""

from __future__ import annotations

import pandas as pd
import gradio as gr

import getting_api as ga


COLUMN_HEADERS = ["樓層", "區域名稱", "總座位", "可用座位"]
BRANCH_CHOICES = ["總館", "稻香分館", "廣慈分館", "文山分館", "西湖分館"]


def _build_dataframe(areas: list[dict[str, object]]) -> pd.DataFrame:
    """Convert the API payload to a Pandas DataFrame with fixed columns."""

    formatted_rows = [
        {
            "樓層": area.get("floorName", "-"),
            "區域名稱": area.get("areaName", "-"),
            "總座位": area.get("totalCount", 0),
            "可用座位": area.get("freeCount", 0),
        }
        for area in areas
    ]

    return pd.DataFrame(formatted_rows, columns=COLUMN_HEADERS)


def search(branch: str) -> pd.DataFrame:
    """Return seat availability for the selected branch."""

    branch_data = ga.filter_branch_areas(branch)
    return _build_dataframe(branch_data)


def build_interface() -> gr.Interface:
    """Create the Gradio interface used by the application."""

    return gr.Interface(
        fn=search,
        inputs=[
            gr.Dropdown(
                BRANCH_CHOICES,
                label="選擇分館",
                info="請選擇要查詢的分館",
            ),
        ],
        outputs=gr.Dataframe(
            label="查詢結果",
            interactive=False,
            row_count=(0, "fixed"),
            col_count=(4, "fixed"),
            wrap=True,
            headers=COLUMN_HEADERS,
        ),
        title="圖書座位查詢系統",
        allow_flagging="never",
    )


def main() -> None:
    """Launch the Gradio demo."""

    build_interface().launch()


if __name__ == "__main__":
    main()

