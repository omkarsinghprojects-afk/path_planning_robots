# AV-SIM — Autonomous Vehicle Research Simulator

A fully browser-based 2D autonomous vehicle simulator built for research and experimentation. 
Run it locally with Docker in one command — no installation, no dependencies.

Simulate multiple autonomous agents navigating complex environments using classical and 
modern path-following algorithms. Design custom paths, place obstacles, set per-agent 
start and end points, write your own controllers in JavaScript, and record the entire 
session as a video or export trajectory data for analysis in Python or MATLAB.

Built with FastAPI + pure JavaScript — no frontend frameworks, no ML libraries required.
Everything runs in a single self-contained HTML file served over a lightweight Python backend.
```

---

**GitHub Topics** (add these as tags on your repo page for discoverability):
```
autonomous-vehicles  robotics  path-planning  simulation  
python  fastapi  docker  research  control-systems  
pure-pursuit  mpc  pid-controller  a-star

```bash
docker-compose up --build
# Open http://localhost:8000
```

Or without Docker:
```bash
pip install -r requirements.txt
uvicorn main:app --port 8000
```

---

## What's New in v2.1

### Algorithms (8 total)
| Algorithm | Description |
|---|---|
| Pure Pursuit | Geometric lookahead-based steering |
| Stanley | Heading + cross-track error control |
| LQR | Linear Quadratic Regulator |
| MPC | Model Predictive Control (horizon 5) |
| PID | Proportional-Integral-Derivative |
| DWA | Dynamic Window Approach |
| Potential Field | Attractive goal + repulsive obstacle fields |
| **Custom ✎** | Write your own JS controller in the panel |

### Custom Controller
Switch to **CUSTOM** algorithm and write JavaScript directly in the panel:
```javascript
function customControl(robot) {
  // robot.x, robot.y, robot.heading, robot.speed, robot.cte
  // path[] — array of {x,y} waypoints
  const target = path[(robot.pathIdx + 3) % path.length];
  const ta = Math.atan2(target.y - robot.y, target.x - robot.x);
  robot.heading += (ta - robot.heading) * 0.08;
  robot.cte = Math.abs(ta - robot.heading) * 5;
}
```
Click **▶ COMPILE & APPLY** to run it live.

### Path Types (8 total)
Loop, Figure-8, Slalom, Zigzag, Spiral, Racetrack, Lemniscate, Custom (click to draw)

### Obstacle Editor
- Shapes: Rectangle, Circle, Triangle, L-Shape
- Custom size (W × H), rotation (degrees), color picker
- Click canvas to place | random scatter | clear all

### Robot Types
Car, Truck, Drone, Bike, Point — each with distinct visuals

### Agent Management
- Up to 8 agents simultaneously
- Per-agent color picker (8 colors)
- Remove individual agents with ✕ button
- Live position/speed display per agent

### Telemetry Tabs
- **DATA** — Speed, heading, CTE, collisions, XY position, distance traveled
- **CHARTS** — Speed, CTE, heading, steer angle, all-agent speed comparison
- **RADAR** — 360° proximity radar with LIDAR overlay
- **LIDAR** — 13-beam distance bars with color-coded proximity

### Environment Controls
- Gravity, friction, wind X/Y sliders
- Map size selector
- Path scale + smoothing

### Algorithm Benchmark
Click **📊 COMPARE** → **▶ RUN BENCHMARK** to automatically test all algorithms and rank by mean CTE.

### Export / Import
- JSON (full session), CSV (per-agent), Path waypoints
- Import path JSON from file
- Session recording → auto-export on stop

### Theme
☀/☾ toggle in header for light/dark mode.

### Keyboard Shortcuts
| Key | Action |
|---|---|
| `SPACE` | Play / Pause |
| `R` | Reset |
| `→` | Step +1 frame |
| `G` | Toggle grid |
| `T` | Toggle trails |
| `L` | Toggle LIDAR |
| `+` / `-` | Zoom |
| `ESC` | Cancel place mode |

---

## Project Structure

```
av-sim-v2/
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── templates/
│   └── index.html      ← entire simulator (self-contained)
└── README.md
```

All logic is in `templates/index.html`. Edit and refresh — no rebuild needed (Docker volume-mounted).
