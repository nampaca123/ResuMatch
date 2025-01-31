import org.springframework.web.bind.annotation.*;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
@RequiredArgsConstructor
public class TextController {
    private final TextService textService;
    
    @PostMapping("/text")
    public void receiveText(@RequestBody TextRequest request) {
        log.info("Received text from file: {}", request.getFilename());
        textService.processText(request.getText(), request.getFilename());
    }
} 