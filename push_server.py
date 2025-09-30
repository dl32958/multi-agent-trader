import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

load_dotenv(override=True)

sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")

mcp = FastMCP("push_server")

class PushModelArgs(BaseModel):
    message: str = Field(description="A brief message to push")

@mcp.tool()
def push(args: PushModelArgs):
    """Send an email notification with this brief message"""
    print(f"Email: {args.message}")
    
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='Trading Alert',
        html_content=f'<strong>{args.message}</strong>'
    )
    
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        return "Email notification sent"
    except Exception as e:
        print(f"Email failed: {e}")
        return "Email notification failed"

if __name__ == "__main__":
    mcp.run(transport='stdio')