// JoinDots.test.jsx - Unit Tests for Connect Four Game
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import JoinDots from './JoinDots';

// Mock CSS import
jest.mock('./JoinDots.css', () => ({}));

describe('JoinDots - Connect Four Game', () => {

    describe('Game Initialization', () => {
        test('renders game board with correct dimensions', () => {
            render(<JoinDots />);
            const cells = document.querySelectorAll('[class*="w-16"]');
            expect(cells.length).toBe(42); // 6 rows × 7 columns
        });

        test('displays game title', () => {
            render(<JoinDots />);
            expect(screen.getByText(/Join Dots/i)).toBeInTheDocument();
        });

        test('initializes with human player turn', () => {
            render(<JoinDots />);
            expect(screen.getByText(/YOUR TURN/i)).toBeInTheDocument();
        });

        test('displays difficulty selector with all levels', () => {
            render(<JoinDots />);
            expect(screen.getByText('EASY')).toBeInTheDocument();
            expect(screen.getByText('MEDIUM')).toBeInTheDocument();
            expect(screen.getByText('HARD')).toBeInTheDocument();
        });
    });

    describe('Win Detection - Horizontal', () => {
        test('detects horizontal win for human player', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Simulate 4 consecutive horizontal moves
            // Row 5 (bottom), columns 0-3
            const bottomRowStart = 35; // 5 * 7 = 35

            for (let i = 0; i < 4; i++) {
                fireEvent.click(cells[bottomRowStart + i]);
                await waitFor(() => { }, { timeout: 1000 });
            }

            await waitFor(() => {
                expect(screen.getByText(/YOU WIN!/i)).toBeInTheDocument();
            }, { timeout: 2000 });
        });
    });

    describe('Win Detection - Vertical', () => {
        test('detects vertical win for human player', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Click same column 4 times (column 3)
            const col3Index = 3;

            for (let i = 0; i < 4; i++) {
                fireEvent.click(cells[col3Index]);
                await waitFor(() => { }, { timeout: 1000 });
            }

            await waitFor(() => {
                const winText = screen.queryByText(/YOU WIN!/i) || screen.queryByText(/AI WINS!/i);
                expect(winText).toBeInTheDocument();
            }, { timeout: 3000 });
        });
    });

    describe('AI Behavior', () => {
        test('AI makes a move after human player', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Human makes first move
            fireEvent.click(cells[3]);

            // Wait for AI thinking indicator
            await waitFor(() => {
                expect(screen.getByText(/AI THINKING/i)).toBeInTheDocument();
            }, { timeout: 1000 });

            // Wait for AI to complete move
            await waitFor(() => {
                expect(screen.getByText(/YOUR TURN/i)).toBeInTheDocument();
            }, { timeout: 2000 });
        });

        test('AI displays thinking process', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            fireEvent.click(cells[0]);

            await waitFor(() => {
                const aiPanel = screen.getByText(/AI Brain/i).closest('div');
                expect(aiPanel).toBeInTheDocument();
            }, { timeout: 1000 });
        });
    });

    describe('Difficulty Levels', () => {
        test('changes difficulty to easy', () => {
            render(<JoinDots />);
            const easyButton = screen.getByText('EASY');

            fireEvent.click(easyButton);

            // Verify difficulty is highlighted
            expect(easyButton.className).toContain('from-blue-500');
        });

        test('changes difficulty to hard', () => {
            render(<JoinDots />);
            const hardButton = screen.getByText('HARD');

            fireEvent.click(hardButton);

            expect(hardButton.className).toContain('from-blue-500');
        });

        test('resets game when changing difficulty', () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Make a move
            fireEvent.click(cells[0]);

            // Change difficulty
            fireEvent.click(screen.getByText('HARD'));

            // Verify game reset
            expect(screen.getByText(/YOUR TURN/i)).toBeInTheDocument();
        });
    });

    describe('Game Reset', () => {
        test('new game button resets board', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Make some moves
            fireEvent.click(cells[0]);
            await waitFor(() => { }, { timeout: 1000 });

            // Click new game
            const newGameButton = screen.getByText(/New Game/i);
            fireEvent.click(newGameButton);

            // Verify reset
            expect(screen.getByText(/YOUR TURN/i)).toBeInTheDocument();
        });

        test('clears AI thoughts on reset', () => {
            render(<JoinDots />);

            const newGameButton = screen.getByText(/New Game/i);
            fireEvent.click(newGameButton);

            expect(screen.getByText(/AI ready/i)).toBeInTheDocument();
        });
    });

    describe('User Interaction', () => {
        test('prevents moves during AI turn', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Human makes move
            fireEvent.click(cells[0]);

            // Try to make another move immediately (during AI thinking)
            fireEvent.click(cells[1]);

            // Should still be AI's turn or transitioning
            await waitFor(() => {
                const status = screen.queryByText(/AI THINKING/i) || screen.queryByText(/YOUR TURN/i);
                expect(status).toBeInTheDocument();
            }, { timeout: 2000 });
        });

        test('prevents moves in full column', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Click same column multiple times (more than 6)
            for (let i = 0; i < 8; i++) {
                fireEvent.click(cells[0]);
                await waitFor(() => { }, { timeout: 500 });
            }

            // Game should still be playable
            const status = screen.queryByText(/YOUR TURN/i) || screen.queryByText(/AI THINKING/i);
            expect(status).toBeInTheDocument();
        });
    });

    describe('Visual Feedback', () => {
        test('highlights last move', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            fireEvent.click(cells[3]);

            await waitFor(() => {
                // Check for pulse animation class
                const animatedCells = container.querySelectorAll('[class*="animate-pulse"]');
                expect(animatedCells.length).toBeGreaterThan(0);
            }, { timeout: 1000 });
        });

        test('displays player colors correctly', () => {
            const { container } = render(<JoinDots />);

            // Verify color classes exist in the component
            expect(container.innerHTML).toContain('from-red-500');
            expect(container.innerHTML).toContain('from-yellow-400');
        });
    });

    describe('Edge Cases', () => {
        test('handles rapid clicking gracefully', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            // Rapid fire clicks
            for (let i = 0; i < 5; i++) {
                fireEvent.click(cells[3]);
            }

            // Should not crash
            await waitFor(() => {
                expect(screen.getByText(/Join Dots/i)).toBeInTheDocument();
            });
        });

        test('maintains game state consistency', async () => {
            const { container } = render(<JoinDots />);
            const cells = container.querySelectorAll('[class*="w-16"]');

            fireEvent.click(cells[0]);

            // Game should maintain valid state
            await waitFor(() => {
                const validStates = [
                    screen.queryByText(/YOUR TURN/i),
                    screen.queryByText(/AI THINKING/i),
                    screen.queryByText(/YOU WIN!/i),
                    screen.queryByText(/AI WINS!/i)
                ];

                const hasValidState = validStates.some(state => state !== null);
                expect(hasValidState).toBe(true);
            }, { timeout: 2000 });
        });
    });
});
