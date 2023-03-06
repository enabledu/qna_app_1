# AUTOGENERATED FROM:
#     'src/queries/accept_answer.edgeql'
#     'src/queries/delete_answer.edgeql'
#     'src/queries/downvote_answer.edgeql'
#     'src/queries/edit_answer.edgeql'
#     'src/queries/get_all_answers.edgeql'
#     'src/queries/get_answers_by_answer_ids.edgeql'
#     'src/queries/get_comments_on_answer.edgeql'
#     'src/queries/undo_accept_answer.edgeql'
#     'src/queries/undo_downvote_answer.edgeql'
#     'src/queries/undo_upvote_answer.edgeql'
#     'src/queries/upvote_answer.edgeql'
# WITH:
#     $ edgedb-py --file


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass

        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class AcceptAnswerResult(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetAllAnswersResult(NoPydanticValidation):
    id: uuid.UUID
    content: str
    upvote: int | None
    downvote: int | None
    author: GetAllAnswersResultAuthor | None
    comments: list[GetAllAnswersResultCommentsItem]
    is_accepted: bool | None


@dataclasses.dataclass
class GetAllAnswersResultAuthor(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetAllAnswersResultCommentsItem(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetCommentsOnAnswerResult(NoPydanticValidation):
    id: uuid.UUID
    content: str
    upvote: int | None
    downvote: int | None
    author: GetAllAnswersResultAuthor | None


async def accept_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            is_accepted := true
        }\
        """,
        id=id,
    )


async def delete_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        delete Answer
        filter .id = <uuid>$id\
        """,
        id=id,
    )


async def downvote_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            downvote := .downvote+1
        }\
        """,
        id=id,
    )


async def edit_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
    content: str,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            content := <str>$content
        }\
        """,
        id=id,
        content=content,
    )


async def get_all_answers(
    executor: edgedb.AsyncIOExecutor,
) -> list[GetAllAnswersResult]:
    return await executor.query(
        """\
        select Answer{
          content,
          upvote,
          downvote,
          author,
          comments,
          is_accepted
        }\
        """,
    )


async def get_answers_by_answer_ids(
    executor: edgedb.AsyncIOExecutor,
    *,
    ids: list[uuid.UUID],
) -> list[GetAllAnswersResult]:
    return await executor.query(
        """\
        select Answer{
          content,
          upvote,
          downvote,
          author,
          comments,
          is_accepted
        } filter .id in array_unpack(<array<uuid>>$ids)\
        """,
        ids=ids,
    )


async def get_comments_on_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> list[GetCommentsOnAnswerResult]:
    return await executor.query(
        """\
        with comment_ids := (select Answer filter .id = <uuid>$id)
        select Comment{
          content,
          upvote,
          downvote,
          author
        } filter .id in comment_ids.comments.id\
        """,
        id=id,
    )


async def undo_accept_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            is_accepted := false
        }\
        """,
        id=id,
    )


async def undo_downvote_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            downvote := .downvote-1
        }\
        """,
        id=id,
    )


async def undo_upvote_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            upvote := .upvote-1
        }\
        """,
        id=id,
    )


async def upvote_answer(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> AcceptAnswerResult | None:
    return await executor.query_single(
        """\
        update Answer
        filter .id = <uuid>$id
        set{
            upvote := .upvote+1
        }\
        """,
        id=id,
    )
