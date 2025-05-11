from typing import Callable


def setup_tasks_from_schedule(
    sender, *, schedule: dict[str, dict[str, Callable | str]]
) -> None:
    for task in schedule.values():
        sender.add_periodic_task(
            task["schedule"],
            task["task"].s(*task.get("args", []), **task.get("kwargs", {})),
            name=task["name"],
        )
