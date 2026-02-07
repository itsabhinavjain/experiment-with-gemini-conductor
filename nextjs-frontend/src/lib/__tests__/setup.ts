import '@testing-library/jest-dom';
import { vi } from 'vitest';

// Mock scrollIntoView since it's not implemented in JSDOM
window.HTMLElement.prototype.scrollIntoView = vi.fn();
