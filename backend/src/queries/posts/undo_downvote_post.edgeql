with
  downvoter := (
    select User
    filter .id = <uuid>$downvoter_id
  ),
  post := (
    update Post
    filter .id = <uuid>$post_id
    set {
      downvoters -= downvoter
    }
  )
select post {
  id,
  upvotes,
  downvotes
}
