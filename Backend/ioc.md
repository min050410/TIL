# IoC란

IoC : 제어의 역전

제어권이 역전 되었다는 뜻이다. 예전에는 의존관계의 제어를 개발자가 직접 해주었다. 그러나 제어권이 컨테이너로 넘어갔고 객체의 생성부터 생명주기의 관리까지 객체에 대한 제어권이 바뀐것을 IoC라고 한다.

```java
import org.springframework.stereotype.Repository;

@Repository
public class BookRepository {

}
```

```java
import org.springframework.stereotype.Service;

@Service
public class BookService {
    BookRepository bookRepository = new BookRepository();
}
```
과거에는 위와 같이 개발자가 직접 제어했다.

하지만 현재에는 제어권이 컨테이너로 넘어갔고 객체의 생성과 생명주기의 관리까지 할 수 있기 때문에 아래와 같은 방식으로 바뀐다.

```java
@Service
public class BookService {
    BookRepository bookRepository;

    @Autowired
    publiic BookService(BookRepository, bookRepository) {
        this.bookRepository = bookRepository;
    }
}