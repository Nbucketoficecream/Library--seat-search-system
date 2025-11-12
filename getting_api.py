"""Utilities for retrieving seat availability information from the API."""

from __future__ import annotations

import logging
from typing import Any, Dict, Iterable, List

import requests


API_URL = "https://seat.tpml.edu.tw/sm/service/getAllArea"
DEFAULT_TIMEOUT = 10


def fetch_all_areas(timeout: int = DEFAULT_TIMEOUT) -> List[Dict[str, Any]]:
    """Return a list of dictionaries describing all seat areas.

    Parameters
    ----------
    timeout:
        The number of seconds to wait for the API to respond.

    Returns
    -------
    list[dict[str, Any]]
        The decoded JSON payload from the API. When the request fails or the
        response format is unexpected an empty list is returned.
    """

    try:
        response = requests.get(API_URL, timeout=timeout)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        logging.warning("⚠️ API 請求失敗：%s", exc)
        return []

    if isinstance(data, list):
        return data

    logging.warning("Unexpected response payload: %s", type(data).__name__)
    return []


def filter_branch_areas(branch: str, areas: Iterable[Dict[str, Any]] | None = None) -> List[Dict[str, Any]]:
    """Filter the API payload and return only the areas for the given branch."""

    source = areas if areas is not None else fetch_all_areas()
    return [area for area in source if area.get("branchName") == branch]
