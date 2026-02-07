import { logger } from '../logger';

// Mocking console methods
const originalLog = console.log;
const originalInfo = console.info;
const originalWarn = console.warn;
const originalError = console.error;

let capturedOutput = '';

function setupMock() {
    capturedOutput = '';
    console.log = (msg: string) => { capturedOutput += msg; };
    console.info = (msg: string) => { capturedOutput += msg; };
    console.warn = (msg: string) => { capturedOutput += msg; };
    console.error = (msg: string) => { capturedOutput += msg; };
}

function teardownMock() {
    console.log = originalLog;
    console.info = originalInfo;
    console.warn = originalWarn;
    console.error = originalError;
}

function testLoggerFormat() {
    setupMock();
    try {
        const testMsg = 'test message';
        logger.info(testMsg);
        
        const captured = capturedOutput;
        teardownMock(); // Restore original console to print results
        
        console.log(`DEBUG: Captured output: "${captured}"`);
        
        // Expected format: [YYYY-MM-DD HH-MM-SS] [INFO] test message
        const regex = /^\[\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2}\] \[INFO\] test message$/;
        if (regex.test(captured)) {
            console.log('SUCCESS: Logger format is correct');
        } else {
            console.error(`FAILURE: Logger format incorrect. Captured: "${captured}"`);
            process.exit(1);
        }
    } catch (e: any) {
        teardownMock();
        console.error(`ERROR: ${e.message}`);
        process.exit(1);
    }
}

try {
    testLoggerFormat();
} catch (e: any) {
    console.error(e.message);
    process.exit(1);
}
