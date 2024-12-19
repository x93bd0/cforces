from typing import Dict, Any

from .blog_entry import BlogEntry
from .comment import Comment
from ..object import Object
from datetime import datetime


class RecentAction(Object):
    """Represents a recent action."""

    __slots__ = ("time_seconds", "blog_entry", "comment")

    time_seconds: int
    blog_entry: BlogEntry
    comment: Comment | None

    @property
    def time(self) -> datetime:
        return datetime.fromtimestamp(self.time_seconds)

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "RecentAction":
        raw_data["blog_entry"] = BlogEntry.from_dict(raw_data["blog_entry"])
        if "comment" in raw_data:
            raw_data["comment"] = Comment.from_dict(raw_data["comment"])
        return RecentAction(**raw_data)
