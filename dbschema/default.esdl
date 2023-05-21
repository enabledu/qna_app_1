module default {
    abstract type Post {
        required property content -> str;
        property upvotes := (select count(.upvoters));
        property downvotes := (select count(.downvoters));
        required link author -> User;
        property views -> int16 {default := 0};
        
        multi link upvoters -> User;
        multi link downvoters -> User;
    }

    type Question extending Post {
        required property title -> str;
        property tags -> array<str>;
        multi link comments -> Comment {
            on target delete allow;
            on source delete delete target;
        }
        multi link answers -> Answer {
            on target delete allow;
            on source delete delete target;
        }
    }

    type Answer extending Post {
        multi link comments -> Comment {
            on target delete allow;
            on source delete delete target;
        }
        property is_accepted -> bool{default := false};
    }

    type Comment extending Post {

    }
}
