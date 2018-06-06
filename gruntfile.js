module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'gm',
          sizes: [{
            width: 500,
            quality: 40
          }, {
            width: 800,
            quality: 40 
          }, {
            width: 1000,
            quality: 40
          }, {
            width: 1600,
            quality: 40
          }]
        },
        
        files: [{
          expand: true,
          src: ['*.jpg'],
          cwd: 'app/static/images_src/',
          dest: 'app/static/images/'
        }]
      }
    },
  });
  
  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.registerTask('default', ['responsive_images']);

};
