import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Service
@RequiredArgsConstructor
public class TextService {
    
    public void processText(String text, String filename) {
        log.info("Processing text from file: {}", filename);
        log.info("Text content (first 500 chars): {}", text.substring(0, Math.min(text.length(), 500)));
        
        // TODO: 
        // 1. 텍스트 전처리
        // 2. OpenAI API 호출
        // 3. DB 저장
    }
} 