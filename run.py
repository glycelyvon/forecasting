#!/usr/bin/env python3
"""
Forecasting Service Runner
Starts the Flask forecasting service
"""

import os
import sys
from app import app, models

def main():
    """Main entry point for the forecasting service"""
    print("=" * 50)
    print("FCM Forecasting Service")
    print("=" * 50)
    
    # Check if models directory exists
    if not os.path.exists('model'):
        os.makedirs('model')
        print("Created model directory")
    
    # Display loaded models
    if models:
        print(f"Loaded models: {list(models.keys())}")
    else:
        print("No models loaded - using fallback predictions")
    
    # Get configuration
    port = int(os.getenv('FORECASTING_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"Starting service on port {port}")
    print(f"Debug mode: {debug}")
    print("=" * 50)
    
    try:
        app.run(host='0.0.0.0', port=port, debug=debug)
    except KeyboardInterrupt:
        print("\nShutting down forecasting service...")
    except Exception as e:
        print(f"Error starting service: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
