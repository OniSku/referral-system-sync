import sqlite3
from typing import List, Optional

def fetch_payments(db_path: str) -> List[dict]:
    """
    Пример исправленной логики сбора транзакций.
    Устранено: неверный формат дат и неправильные фильтры статусов.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        # Мы заменили unixepoch на прямое чтение, так как формат в БД изменился
        query = """
            SELECT payment_id, user_id, 
            date(updated_at) AS payment_date 
            FROM transactions 
            WHERE status IN ('paid', 'succeeded')
        """
        cur = conn.execute(query)
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()

def get_referrer(db_path: str, user_id: int) -> Optional[int]:
    """
    Поиск пригласителя по глобальному ID пользователя.
    """
    conn = sqlite3.connect(db_path)
    try:
        # Исправлено: поиск теперь идет по telegram_id, а не по внутреннему PK
        cur = conn.execute("SELECT referrer_id FROM users WHERE telegram_id = ?", (user_id,))
        row = cur.fetchone()
        return row[0] if row else None
    finally:
        conn.close()