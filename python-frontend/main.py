import asyncio
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.live import Live
from rich.prompt import Prompt
from client import backend_client

console = Console()

async def main(console_override=None):
    global console
    if console_override:
        console = console_override
        
    console.print(Panel("[bold green]Claude Agent SDK CLI[/bold green]", expand=False))
    console.print("Type 'exit' or 'quit' to end the conversation.")
    
    current_session_id = None
    
    while True:
        try:
            user_input = Prompt.ask("[bold blue]You[/bold blue]")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            console.print(Text("Thinking...", style="dim"))
            
            # This will hold the collected response text and thinking blocks
            full_response_text = ""
            thinking_blocks = []
            
            with Live(console=console, screen=False, refresh_per_second=4) as live:
                agent_response_stream = backend_client.stream_chat(user_input, current_session_id)
                
                async for chunk in agent_response_stream:
                    chunk_type = chunk.get("type")
                    chunk_content = chunk.get("content")

                    if chunk_type == "session_id":
                        current_session_id = chunk_content
                    elif chunk_type == "thinking":
                        thinking_blocks.append(chunk_content)
                        # Display latest thinking block in a panel
                        live.update(Panel(
                            Text("\n".join(thinking_blocks), style="yellow"), 
                            title="[bold yellow]Claude's Thinking[/bold yellow]", 
                            border_style="yellow",
                            expand=False
                        ))
                    elif chunk_type == "text":
                        full_response_text += chunk_content
                        # Update live display with response and thinking
                        from rich.console import Group
                        
                        renderables = []
                        if thinking_blocks:
                            renderables.append(Panel(
                                Text("\n".join(thinking_blocks), style="yellow"),
                                title="[bold yellow]Claude's Thinking[/bold yellow]",
                                border_style="yellow",
                                expand=False
                            ))
                        
                        renderables.append(Text(full_response_text, style="green"))
                        
                        live.update(Group(*renderables))
                    elif chunk_type == "error":
                        console.print(Panel(f"[bold red]Error:[/bold red] {chunk_content}", border_style="red"))
                        break # Exit on error
            
            if full_response_text:
                console.print(Text("\n[bold green]Claude:[/bold green] ", style="green") + Text(full_response_text))
            
        except KeyboardInterrupt:
            console.print("\n[bold red]Conversation interrupted.[/bold red]")
            break
        except Exception as e:
            console.print(Panel(f"[bold red]An unexpected error occurred:[/bold red] {e}", border_style="red"))
            break

if __name__ == "__main__":
    asyncio.run(main())