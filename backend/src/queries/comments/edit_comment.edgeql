with date_modified := datetime_of_statement()
update Comment
filter .id = <uuid>$comment_id
set {
    content := <str>$content,
  date_modified := date_modified
}