select Question {
  id,
  author: {
    id,
    username
  },
  title,
  content,
  tags,
  views,
  upvotes,
  downvotes,
  date_created,
  date_modified
}