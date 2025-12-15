// Camera utilities for face recognition

class CameraManager {
    constructor(videoElement, constraints = { video: true }) {
        this.videoElement = videoElement;
        this.constraints = constraints;
        this.stream = null;
    }
    
    // Start camera
    async start() {
        try {
            this.stream = await navigator.mediaDevices.getUserMedia(this.constraints);
            this.videoElement.srcObject = this.stream;
            return true;
        } catch (error) {
            console.error('Error starting camera:', error);
            return false;
        }
    }
    
    // Stop camera
    stop() {
        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
            this.stream = null;
        }
    }
    
    // Capture frame
    captureFrame() {
        if (!this.videoElement || !this.videoElement.videoWidth) {
            return null;
        }
        
        const canvas = document.createElement('canvas');
        canvas.width = this.videoElement.videoWidth;
        canvas.height = this.videoElement.videoHeight;
        
        const context = canvas.getContext('2d');
        context.drawImage(this.videoElement, 0, 0, canvas.width, canvas.height);
        
        return {
            dataUrl: canvas.toDataURL('image/jpeg'),
            canvas: canvas
        };
    }
    
    // Toggle camera
    async toggle() {
        if (this.stream) {
            this.stop();
            return false;
        } else {
            return await this.start();
        }
    }
}

// Export the class
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CameraManager;
}
