import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta, date

# Define the phases and durations
phases = [
    ("Discovery & Planning", 2),
    ("Infrastructure Setup", 2),
    ("Value Stream Integration", 4),
    ("Scalability & Fault Tolerance Testing", 3),
    ("Monitoring & Operational Readiness", 2),
    ("Go Live", 1),
    ("Continuous Improvement", 0)  # Ongoing phase, doesn't have an end date
]

# Start date for the timeline
start_date = date(2025, 10, 16)

# Calculate start and end dates for each phase
phase_dates = []
current_start = start_date
for phase, duration in phases:
    phase_end = current_start + timedelta(weeks=duration)
    phase_dates.append((phase, current_start, phase_end))
    current_start = phase_end  # Update the start date for the next phase

# Prepare the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each phase as a horizontal bar
for i, (phase, start, end) in enumerate(phase_dates):
    ax.barh(i, (end - start).days, left=start, height=0.8, label=phase)

# Add labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Phase')
ax.set_title('Event Hub Deployment Roadmap')
ax.set_yticks(range(len(phases)))
ax.set_yticklabels([phase[0] for phase in phase_dates])

# Format the x-axis to display dates
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator())
fig.autofmt_xdate()

# Add a grid for easier reading
ax.grid(True, axis='x', linestyle='--', alpha=0.5)

# Display the chart
plt.tight_layout()
plt.savefig('event_hub_timeline.png', dpi=300)  #
