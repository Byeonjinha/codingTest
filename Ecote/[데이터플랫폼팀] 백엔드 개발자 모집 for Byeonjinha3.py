회원 목록 /users -> GET
회원 등록 폼 /users/new -> GET
회원 등록 /users/new, /members -> POST
회원 조회 /users/{id} -> GET
회원 수정 폼 /users/{id}/edit -> GET
회원 수정 /users/{id}/edit, /members/{id} -> POST
회원 삭제 /users/{id}/delete -> POST
curl -X POST "localhost:9200/[인덱스이름]/_delete_by_query?conflicts=proceed&pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}'
파일 목록 /files -> GET
파일 조회 /files/{filename} -> GET
파일 등록 /files/{filename} -> PUT
파일 삭제 /files/{filename} -> DELETE
파일 대량 등록 /files -> POST


query{
      users{
            user_no
            user_id
            user_name
      }
    }
