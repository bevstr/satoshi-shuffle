Version 1.1 - March 22, 2025

# Satoshi Shuffle (BlockClock Control) - Project Roadmap

## Project Overview
Satoshi Shuffle provides tools to control Coinkite BlockClock Mini/Micro devices by displaying custom text messages that rotate on a configurable schedule. The project has evolved from a bash script to a full web application with multiple deployment options.

## Current Status
- ✅ Original bash script implementation completed
- ✅ Python conversion of the bash script completed
- ✅ Web interface developed and functional
- ✅ Dynamic port configuration implemented
- ✅ Docker configuration completed
- ✅ Installation script with multiple deployment options
- ✅ Log rotation system implemented
- ✅ Device connectivity checking functionality
- ✅ GitHub repository structure established
- ✅ Comprehensive documentation created

## Components

### 1. Bash Script (Original) - COMPLETED
- Takes a configuration file to define device IPs, text messages, and timing
- Controls multiple BlockClock devices simultaneously
- Rotates custom text messages on a specified schedule

### 2. Python Implementation - COMPLETED
- Core functionality ported from bash to Python
- Supports the same configuration format
- Improved error handling and logging

### 3. Web Application - COMPLETED
- **Framework:** Flask
- **Features:**
  - Browser-based user interface
  - Configuration through UI forms
  - Device status monitoring
  - Background service for text rotation
  - Multi-device management
  - Log rotation with archiving
  - Dark mode support

### 4. Deployment Options - COMPLETED
- **Direct installation:** Running Python app directly
- **Docker container:** Simplified deployment
- **One-click install script:** For non-technical users

## Technical Architecture

### Core Python Module - COMPLETED
- **Device communication:** Handles API calls to BlockClock devices
- **Rotation service:** Manages the text rotation scheduling
- **Configuration management:** Handles loading/saving settings

### Web Application - COMPLETED
- **Flask application:** Provides the web interface
- **Background service:** Handles the text rotation in the background
- **Monitoring system:** Real-time status updates

### Docker Setup - COMPLETED
- Application container with all dependencies
- Volume for persistent configuration storage
- Easy deployment across platforms

## Project Structure
```
satoshi-shuffle/
├── README.md                      # Main project documentation
├── LICENSE                        # MIT license
├── CHEATSHEET.md                  # Command-line reference
├── config.py                      # Core configuration handling
├── config/                        # Configuration directory
│   └── blockclock.conf            # Main configuration file
├── docker/                        # Docker configuration
│   ├── Dockerfile                 # Container definition
│   ├── README.md                  # Docker setup instructions
│   └── docker-compose.yml         # Container orchestration
├── docs/                          # Documentation
│   ├── configuration.md           # Configuration guide
│   ├── installation-docker.md     # Docker installation guide
│   ├── installation-python.md     # Python installation guide
│   ├── installation-script.md     # One-click script guide
│   ├── troubleshooting.md         # Troubleshooting guide
│   └── Satoshi-Shuffle-roadmap.md # Project roadmap
├── filter_output.py               # Log filtering utility
├── Images/                        # Screenshots and images
│   └── Dashboard.png              # Main interface screenshot
├── install.py                     # Installation script
├── logs/                          # Logging directory
│   └── archive/                   # Archived log files
├── python/                        # Core Python module
│   └── blockclock.py              # Main BlockClock control code
├── requirements.txt               # Python dependencies
├── start_SatoshiShuffle.sh        # Startup script
└── webapp/                        # Web application
    ├── __init__.py                # Flask app initialization
    ├── blockclock_web.py          # Web app entry point
    ├── routes.py                  # Web routes and API endpoints
    ├── app/                       # Application components
        ├── static/                # Static web assets
        │   └── css/
        │       └── styles.css     # CSS styling
        └── templates/             # HTML templates
            ├── base.html          # Base template
            ├── index.html         # Main page
            └── settings.html      # Settings page
```

## Completed Tasks

### Code Enhancements
- ✅ Implemented rate limiting mechanism to protect devices from too frequent text changes
- ✅ Added synchronization management for text rotation
- ✅ Enhanced error handling for network issues

### Feature Additions
- ✅ Added configuration backup/restore functionality
- ✅ Implemented log rotation with configurable settings
- ✅ Added theme preferences with dark mode support

### UI Improvements
- ✅ Implemented dark/light mode toggle functionality
- ✅ Added visual indicators for system status
- ✅ Created intuitive settings interface with tabbed navigation

### Documentation
- ✅ Created comprehensive README
- ✅ Added detailed installation guides
- ✅ Created configuration documentation
- ✅ Added troubleshooting guide
- ✅ Created command-line cheatsheet

## Future Enhancements (If Needed)
1. **Potential Improvements**
   - ⏳ Add statistics tracking for device uptime/performance
   - ⏳ Enhance mobile responsiveness
   - ⏳ Implement notification system for critical errors
   - ⏳ Improve log display and filtering

2. **Testing**
   - ⏳ Implement automated testing
   - ⏳ Conduct user testing for UI improvements
   - ⏳ Test installation on various platforms

3. **GitHub Repository Enhancements**
   - ⏳ Create issue templates
   - ⏳ Set up automated builds
   - ⏳ Configure release notes generation

## Technical Requirements
- Python 3.6+ for all Python components
- Flask for the web framework
- Docker & Docker Compose for containerized deployment
- Linux or macOS (Windows not officially supported)

## Installation Options
1. **One-Click Installation** - Guided setup process
2. **Docker Installation** - For users familiar with Docker
3. **Direct Python Installation** - For users who prefer manual setup

## Port Configuration
The web application uses port 5001 by default. If this port is already in use on your system, you may encounter errors when starting the application.

### Changing the Port
To change the port, open the `webapp/blockclock_web.py` file and modify the port number:

```python
app.run(debug=False, host='0.0.0.0', port=5001, use_reloader=True)
```

Change `port=5001` to another port, such as 5002 or 5003.

### Accessing the Web Interface
After starting the web interface, you can access it using:

- **From your local machine:** http://localhost:5001 (or whatever port you configured)
- **From other devices on your network:** http://your-ip-address:5001 (replace "your-ip-address" with your computer's IP address)

## Future Considerations
- Support for additional BlockClock features as they are released
- Integration with other Bitcoin-related services
- Advanced scheduling options
- Mobile app companion

---
*Last updated: March 22, 2025*





























current roadmap version

# Satoshi Shuffle (BlockClock Control) - Updated Project Roadmap

## Project Overview
Satoshi Shuffle provides tools to control Coinkite BlockClock Mini/Micro devices by displaying custom text messages that rotate on a configurable schedule. The project has evolved from a bash script to a full web application with multiple deployment options.

## Current Status
- ✅ Original bash script implementation completed
- ✅ Python conversion of the bash script completed
- ✅ Web interface developed and functional
- ✅ Dynamic port configuration implemented
- ✅ Docker configuration completed
- ✅ Installation script with multiple deployment options
- ✅ Log rotation system implemented
- ✅ Device connectivity checking functionality

## Components

### 1. Bash Script (Original) - COMPLETED
- Takes a configuration file to define device IPs, text messages, and timing
- Controls multiple BlockClock devices simultaneously
- Rotates custom text messages on a specified schedule

### 2. Python Implementation - COMPLETED
- Core functionality ported from bash to Python
- Supports the same configuration format
- Improved error handling and logging

### 3. Web Application - COMPLETED
- **Framework:** Flask
- **Features:**
  - Browser-based user interface
  - Configuration through UI forms
  - Device status monitoring
  - Background service for text rotation
  - Multi-device management
  - Log rotation with archiving
  - Dark mode support

### 4. Deployment Options - COMPLETED
- **Direct installation:** Running Python app directly
- **Docker container:** Simplified deployment
- **One-click install script:** For non-technical users

## Technical Architecture

### Core Python Module - COMPLETED
- **Device communication:** Handles API calls to BlockClock devices
- **Rotation service:** Manages the text rotation scheduling
- **Configuration management:** Handles loading/saving settings

### Web Application - COMPLETED
- **Flask application:** Provides the web interface
- **Background service:** Handles the text rotation in the background
- **Monitoring system:** Real-time status updates

### Docker Setup - COMPLETED
- Application container with all dependencies
- Volume for persistent configuration storage
- Easy deployment across platforms

## Project Structure
```
Satoshi-Shuffle/
├── README.md                      # Main project documentation
├── blockclock-roadmap.md          # Project roadmap
├── config.py                      # Core configuration handling
├── config/                        # Configuration directory
│   └── blockclock.conf            # Main configuration file
├── docker/                        # Docker configuration
│   ├── Dockerfile                 # Container definition
│   ├── README.md                  # Docker setup instructions
│   └── docker-compose.yml         # Container orchestration
├── filter_output.py               # Log filtering utility
├── install.py                     # Installation script
├── logs/                          # Logging directory
│   ├── blockclock.log             # Current log file
│   └── blockclock.log.2025-03-15  # Archived log file
├── python/                        # Core Python module
│   └── blockclock.py              # Main BlockClock control code
├── requirements.txt               # Python dependencies
├── start_SatoshiShuffle.sh        # Startup script
└── webapp/                        # Web application
    ├── __init__.py                # Flask app initialization
    ├── blockclock_web.py          # Web app entry point
    ├── routes.py                  # Web routes and API endpoints
    ├── static/                    # Static web assets
    │   └── css/
    │       └── styles.css         # CSS styling
    └── templates/                 # HTML templates
        ├── base.html              # Base template
        ├── index.html             # Main page
        └── settings.html          # Settings page
```

## Next Steps

### Completed Tasks
1. **Code Enhancements**
   - ✅ Implemented rate limiting mechanism to protect devices from too frequent text changes
   - ✅ Added synchronization management for text rotation

2. **Feature Additions**
   - ✅ Added configuration backup/restore functionality
   - ✅ Implemented log rotation with configurable settings
   - ✅ Added theme preferences with dark mode support

3. **UI Improvements**
   - ✅ Implemented dark/light mode toggle functionality
   - ✅ Added visual indicators for system status
   - ✅ Created intuitive settings interface with tabbed navigation

### Future Enhancements (If Needed)
1. **Potential Improvements**
   - ⏳ Add statistics tracking for device uptime/performance
   - ⏳ Enhance mobile responsiveness
   - ⏳ Implement notification system for critical errors
   - ⏳ Improve log display and filtering

### Medium-term Tasks
1. **Documentation**
   - ⏳ Complete inline code documentation
   - ⏳ Create comprehensive user guide
   - ⏳ Add troubleshooting section
   - ⏳ Create installation walkthrough videos

2. **Testing**
   - ⏳ Implement automated testing
   - ⏳ Conduct user testing for UI improvements
   - ⏳ Test installation on various platforms

### Final Steps
1. **GitHub Repository Setup**
   - ⏳ Create repository with proper structure
   - ⏳ Add contribution guidelines
   - ⏳ Set up release workflow
   - ⏳ Create issue templates

2. **Release Management**
   - ⏳ Create versioning strategy
   - ⏳ Set up automated builds
   - ⏳ Configure release notes generation

## Technical Requirements
- Python 3.10+ for all Python components
- Flask for the web framework
- Docker & Docker Compose for containerized deployment
- Linux or macOS (Windows not officially supported)

## Installation Options
1. **One-Click Installation** - Guided setup process
2. **Docker Installation** - For users familiar with Docker
3. **Direct Python Installation** - For users who prefer manual setup
4. **Bash Script** - Lightweight option for advanced users

## Port Configuration
The web application uses port 5001 by default. If this port is already in use on your system, you may encounter errors when starting the application.

### Changing the Port
To change the port, open the `blockclock_web.py` file and modify the port number:

```python
app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=True)
```

Change `port=5001` to another port, such as 5002 or 5003.

### Accessing the Web Interface
After starting the web interface, you can access it using:

- **From your local machine:** http://localhost:5001 (or whatever port you configured)
- **From other devices on your network:** http://your-ip-address:5001 (replace "your-ip-address" with your computer's IP address)

## Future Considerations
- Support for additional BlockClock features as they are released
- Integration with other Bitcoin-related services
- Advanced scheduling options
- Mobile app companion

---
*Last updated: March 21, 2025*



previos version of roadmap below

# Satoshi Shuffle (BlockClock Control) - Updated Project Roadmap

## Project Overview
Satoshi Shuffle provides tools to control Coinkite BlockClock Mini/Micro devices by displaying custom text messages that rotate on a configurable schedule. The project has evolved from a bash script to a full web application with multiple deployment options.

## Current Status
- ✅ Original bash script implementation completed
- ✅ Python conversion of the bash script completed
- ✅ Web interface developed and functional
- ✅ Dynamic port configuration implemented
- ✅ Docker configuration completed
- ✅ Installation script with multiple deployment options
- ✅ Log rotation system implemented
- ✅ Device connectivity checking functionality

## Components

### 1. Bash Script (Original) - COMPLETED
- Takes a configuration file to define device IPs, text messages, and timing
- Controls multiple BlockClock devices simultaneously
- Rotates custom text messages on a specified schedule

### 2. Python Implementation - COMPLETED
- Core functionality ported from bash to Python
- Supports the same configuration format
- Improved error handling and logging

### 3. Web Application - COMPLETED
- **Framework:** Flask
- **Features:**
  - Browser-based user interface
  - Configuration through UI forms
  - Device status monitoring
  - Background service for text rotation
  - Multi-device management
  - Log rotation with archiving
  - Dark mode support

### 4. Deployment Options - COMPLETED
- **Direct installation:** Running Python app directly
- **Docker container:** Simplified deployment
- **One-click install script:** For non-technical users

## Technical Architecture

### Core Python Module - COMPLETED
- **Device communication:** Handles API calls to BlockClock devices
- **Rotation service:** Manages the text rotation scheduling
- **Configuration management:** Handles loading/saving settings

### Web Application - COMPLETED
- **Flask application:** Provides the web interface
- **Background service:** Handles the text rotation in the background
- **Monitoring system:** Real-time status updates

### Docker Setup - COMPLETED
- Application container with all dependencies
- Volume for persistent configuration storage
- Easy deployment across platforms

## Project Structure

BevosM4:Blockclock-project bitty$ find . -type f -not -path "*/\.*" -not -path "*/venv/*" -not -path "*/node_modules/*" | sort | sed -e 's/[^-][^\/]*\//│   /g' -e 's/│   \([^│]\)/├── \1/g' -e 's/│   │/│   │/g' -e 's/\(│   \)*│/\1└/g


```
Satoshi-Shuffle/
├── README.md                      # Main project documentation
├── blockclock-roadmap.md          # Project roadmap
├── config.py                      # Core configuration handling
├── config/                        # Configuration directory
│   └── blockclock.conf            # Main configuration file
├── docker/                        # Docker configuration
│   ├── Dockerfile                 # Container definition
│   ├── README.md                  # Docker setup instructions
│   └── docker-compose.yml         # Container orchestration
├── filter_output.py               # Log filtering utility
├── install.py                     # Installation script
├── logs/                          # Logging directory
│   ├── blockclock.log             # Current log file
│   └── blockclock.log.2025-03-15  # Archived log file
├── python/                        # Core Python module
│   └── blockclock.py              # Main BlockClock control code
├── requirements.txt               # Python dependencies
├── start_SatoshiShuffle.sh        # Startup script
└── webapp/                        # Web application
    ├── __init__.py                # Flask app initialization
    ├── blockclock_web.py          # Web app entry point
    ├── routes.py                  # Web routes and API endpoints
    ├── static/                    # Static web assets
    │   └── css/
    │       └── styles.css         # CSS styling
    └── templates/                 # HTML templates
        ├── base.html              # Base template
        ├── index.html             # Main page
        └── settings.html          # Settings page
```

## Next Steps

### Short-term Tasks
1. **Code Enhancements**
   - ⏳ Improve synchronization after manual text sending
   - ⏳ Optimize rate limiting mechanism
   - ⏳ Enhance error handling for network issues

2. **Feature Additions**
   - ⏳ Add configuration backup/restore functionality
   - ⏳ Implement notification system for critical errors
   - ⏳ Add statistics tracking for device uptime/performance

3. **UI Improvements**
   - ⏳ Enhance mobile responsiveness
   - ⏳ Refine dark/light mode toggle functionality
   - ⏳ Add visual indicators for system status
   - ⏳ Improve log display and filtering

### Medium-term Tasks
1. **Documentation**
   - ⏳ Complete inline code documentation
   - ⏳ Create comprehensive user guide
   - ⏳ Add troubleshooting section
   - ⏳ Create installation walkthrough videos

2. **Testing**
   - ⏳ Implement automated testing
   - ⏳ Conduct user testing for UI improvements
   - ⏳ Test installation on various platforms

### Final Steps
1. **GitHub Repository Setup**
   - ⏳ Create repository with proper structure
   - ⏳ Add contribution guidelines
   - ⏳ Set up release workflow
   - ⏳ Create issue templates

2. **Release Management**
   - ⏳ Create versioning strategy
   - ⏳ Set up automated builds
   - ⏳ Configure release notes generation

## Technical Requirements
- Python 3.10+ for all Python components
- Flask for the web framework
- Docker & Docker Compose for containerized deployment
- Linux or macOS (Windows not officially supported)

## Installation Options
1. **One-Click Installation** - Guided setup process
2. **Docker Installation** - For users familiar with Docker
3. **Direct Python Installation** - For users who prefer manual setup
4. **Bash Script** - Lightweight option for advanced users

## Port Configuration
The web application uses port 5001 by default. If this port is already in use on your system, you may encounter errors when starting the application.

### Changing the Port
To change the port, open the `blockclock_web.py` file and modify the port number:

```python
app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=True)
```

Change `port=5001` to another port, such as 5002 or 5003.

### Accessing the Web Interface
After starting the web interface, you can access it using:

- **From your local machine:** http://localhost:5001 (or whatever port you configured)
- **From other devices on your network:** http://your-ip-address:5001 (replace "your-ip-address" with your computer's IP address)

## Future Considerations
- Support for additional BlockClock features as they are released
- Integration with other Bitcoin-related services
- Advanced scheduling options
- Mobile app companion

---
*Last updated: March 21, 2025*















previous roadmap below

 BlockClock Control Project Roadmap

## Project Overview
This project provides tools to control Coinkite BlockClock Mini/Micro devices by displaying custom text messages that rotate on a configurable schedule. The project has evolved from a bash script to a full web application with multiple deployment options.

## Current Status
- ✅ Original bash script implementation completed
- ✅ Python conversion of the bash script completed
- ✅ Web interface developed and functional
- ✅ Dynamic port configuration implemented
- ⏳ GitHub repository structure planning completed but not implemented

## Recent Improvements
- **Log Rotation System**: Implemented a comprehensive log rotation system that maintains recent logs in the main directory and archives older logs, with automatic cleanup of logs older than 30 days.

## Components

### 1. Bash Script (Original)
- Takes a configuration file to define device IPs, text messages, and timing
- Controls multiple BlockClock devices simultaneously
- Rotates custom text messages on a specified schedule

### 2. Python Implementation
- Core functionality ported from bash to Python
- Supports the same configuration format
- Improved error handling and logging

### 3. Web Application (Current Focus)
- **Framework:** Flask
- **Features:**
  - Browser-based user interface
  - Configuration through UI forms
  - Device status monitoring
  - Background service for text rotation
  - Multi-device management
  - Log rotation with archiving

### 4. Deployment Options
- **Direct installation:** Running Python app directly
- **Docker container:** Simplified deployment (planned)
- **One-click install script:** For non-technical users (planned)

## Technical Architecture

### Core Python Module
- **Device communication:** Handles API calls to BlockClock devices
- **Rotation service:** Manages the text rotation scheduling
- **Configuration management:** Handles loading/saving settings

### Web Application
- **Flask application:** Provides the web interface
- **Database:** Stores device configurations and text options
- **Background service:** Handles the text rotation in the background

### Planned Docker Setup
- Application container with all dependencies
- Volume for persistent configuration storage
- Easy deployment across platforms

## Planned Repository Structure
```
blockclock-control/
├── README.md              # Main documentation
├── INSTALL.md             # Installation instructions
├── LICENSE
├── bash/                  # Original bash implementation
│   ├── blockclock.sh      # Original script
│   ├── blockclock.conf    # Example configuration
│   └── README.md          # Bash-specific instructions
├── python/                # Python implementation (CLI)
│   ├── blockclock/        # Core Python module
│   │   ├── __init__.py
│   │   ├── device.py      # Device communication
│   │   ├── rotation.py    # Text rotation logic
│   │   └── config.py      # Configuration management
│   ├── setup.py           # For pip installation
│   ├── requirements.txt   # Python dependencies
│   └── README.md          # Python CLI instructions
├── webapp/                # Web application
│   ├── app/               # Flask application
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── service.py     # Background service
│   │   ├── templates/     # HTML templates
│   │   └── static/        # CSS, JavaScript, etc.
│   ├── requirements.txt   # Web app dependencies
│   └── README.md          # Web app instructions
├── blockclock_web.py      # Web app entry point with dynamic port allocation
├── docker/                # Docker configuration
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md          # Docker instructions
└── install.py             # One-click install script
```

## Next Steps

### Immediate Tasks
1. ✅ Implement log rotation for better log management - COMPLETED
2. Fix synchronization issues when manually sending text via web UI
3. Consolidate configuration files to a single location
4. Test the application thoroughly with multiple devices

### Short-term Tasks
1. Create Docker configuration for containerized deployment
2. Develop the one-click install script
3. Prepare comprehensive documentation for each component

### Future Plans
1. Create GitHub repository and upload the complete project
2. Add user authentication to the web interface (if needed)
3. Improve the UI with real-time updates and visualizations
4. Consider adding additional features based on user feedback

## Technical Requirements
- Python 3.10+ for all Python components
- Flask for the web framework
- Docker & Docker Compose for containerized deployment
- Linux or macOS (Windows not officially supported)

## Installation Options (Preview)
1. **One-Click Installation** - Guided setup process
2. **Docker Installation** - For users familiar with Docker
3. **Direct Python Installation** - For users who prefer manual setup
4. **Bash Script** - Lightweight option for advanced users

## Port Configuration
The web application uses port 5001 by default. If this port is already in use on your system, you may encounter errors when starting the application.

### Changing the Port
To change the port, open the `blockclock_web.py` file and modify the port number:

```python
app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=True)
```

Change `port=5001` to another port, such as 5002 or 5003.

### Accessing the Web Interface
After starting the web interface, you can access it using:

- **From your local machine:** http://localhost:5001 (or whatever port you configured)
- **From other devices on your network:** http://your-ip-address:5001 (replace "your-ip-address" with your computer's IP address)

### Finding Your IP Address
To find your computer's IP address:

**macOS**: Open Terminal and enter: `ipconfig getifaddr en0`
**Linux**: Open Terminal and enter: `hostname -I` or `ip addr show`
**Windows**: Open Command Prompt and enter: `ipconfig`

---
*Note: This roadmap will be updated as the project progresses.*


