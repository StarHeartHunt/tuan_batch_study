from loguru import logger

from constants import logger_config
from utils import get_chapter_id, get_sign, get_token, save_history

logger.configure(**logger_config)

if __name__ == "__main__":
    for mid in open("mid.txt"):
        # 跳过空行
        if mid.isspace():
            continue
        logger.info(f"开始执行{mid}的学习记录上报")
        try:
            cid = get_chapter_id()
            # logger.debug(cid)
            sign = get_sign(mid)
            # logger.debug(mid, sign)
            token = get_token(sign)
            # logger.debug(token)
            res = save_history(token, cid)
            # logger.debug(res)
        except Exception:
            logger.opt(exception=True).info("请求时发生错误")
            continue

        if res["errno"] == 0:
            logger.info("保存观看记录成功")
        else:
            logger.error(f"响应发生错误({res['errno']}): {res['errmsg']}")
