document.addEventListener('DOMContentLoaded', function() {
    const imageElement = document.getElementById('s3-image');
    const loadingElement = document.getElementById('loading');
    
    // The AWS signed URL
    const signedUrl = 'https://alpha-bake-loras.s3.amazonaws.com/LORA_LOGGER/9129/9454/tryon/123865/5276576241746494515.jpg?AWSAccessKeyId=AKIA3CTOLBCIXYCF4B2Q&Signature=2sNfQW%2Ff0VEJuN0tcIgbNjo1ybY%3D&Expires=1778030515';
    
    // Set the image source to the signed URL
    imageElement.src = signedUrl;
    
    // Handle image load success
    imageElement.onload = function() {
        // Hide loading spinner
        loadingElement.style.display = 'none';
        // Show the image
        imageElement.style.display = 'block';
        console.log('Image loaded successfully');
    };
    
    // Handle image load failure
    imageElement.onerror = function() {
        loadingElement.innerHTML = '<p>Error loading image. The signed URL may have expired.</p>';
        console.error('Failed to load the image');
    };
}); 