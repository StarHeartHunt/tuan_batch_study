import httpx

from constants import (
    api_headers,
    get_sign_url,
    get_token_url,
    get_chapter_url,
    save_history_url,
    youthstudy_headers,
)


def get_sign(mid):
    response = httpx.get(
        get_sign_url,
        params={"mid": str(mid)},
        headers=api_headers,
        timeout=30.0,
        # proxies="http://127.0.0.1:8888",
        # verify=False,
    )
    sign_url = response.json()["youthLearningUrl"]
    sign = sign_url.split("?")
    # logger.debug(sign[1][5:])
    return sign[1][5:]


def get_token(sign):
    response = httpx.post(
        get_token_url,
        headers=youthstudy_headers,
        data={"sign": sign},
        timeout=30.0,
        # proxies="http://127.0.0.1:8888",
        # verify=False,
    )
    # logger.debug(j["data"]["entity"]["token"])
    return response.json()["data"]["entity"]["token"]


def get_chapter_id():
    response = httpx.get(
        get_chapter_url,
        headers={"X-Litemall-IdentiFication": "young"},
        timeout=30.0,
        # proxies="http://127.0.0.1:8888",
        # verify=False,
    )
    return response.json()["data"]["entity"]["id"]


def save_history(token, cid):
    headers = youthstudy_headers
    headers["X-Litemall-Token"] = token
    response = httpx.post(
        save_history_url,
        headers=headers,
        data={"chapterId": str(cid)},
        timeout=30.0,
        # proxies="http://127.0.0.1:8888",
        # verify=False,
    )
    return response.json()
