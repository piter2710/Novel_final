```mermaid
erDiagram
    USERS ||--o{ COMMENTS : writes
    USERS ||--o{ REVIEWS : writes
    USERS ||--o{ COMMENT_LIKES : gives

    NOVELS ||--o{ CHAPTERS : contains
    NOVELS ||--o{ COMMENTS : has
    NOVELS ||--o{ REVIEWS : has
    NOVELS ||--o{ NOVEL_TAGS : tagged

    CHAPTERS ||--o{ COMMENTS : has

    COMMENTS ||--o{ COMMENTS : replies_to

    COMMENTS ||--o{ COMMENT_LIKES : receives

    TAGS ||--o{ NOVEL_TAGS : categorizes
```