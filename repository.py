from sqlalchemy import select

from database_01 import new_session, TaskOrm
from schemas_01 import STask, STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()  # сохраняем в БД, но не отправляем в пакеты
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [
                STask.model_validate(task_model) for task_model in task_models
            ]
            return task_schemas
