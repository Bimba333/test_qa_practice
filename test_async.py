import pytest
from async_test import get_todos

@pytest.mark.asyncio
async def test_get_todos_count():
    result = await get_todos([1, 2, 3, 4, 5])
    assert len(result) == 5

@pytest.mark.asyncio
async def test_get_todo_has_fields():
    result = await get_todos([1, 2, 3, 4, 5])
    for todo in result:
        assert "id" in todo
        assert "title" in todo
        assert "completed" in todo