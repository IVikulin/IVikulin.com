var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var cleanCSS = require('gulp-clean-css');
var browserify = require('gulp-browserify');
var imagemin = require('gulp-imagemin');

var path = {
  JS:   './jsapps/main.js',
  CSS:  './styles/main.scss',
  IMG:  './images/**/*.*',
  DEST: './public/static'
};

gulp.task('default', ['styles', 'scripts', 'img'], function () {
  gulp.watch(path.JS, ['scripts']);
  gulp.watch(path.CSS, ['styles']);
  gulp.watch(path.SVG, ['svg']);
  gulp.watch(path.IMG, ['img']);
});

gulp.task('light', ['styles', 'scripts'], function () {
  gulp.watch(path.CSS, function() {
    setTimeout(function () {
      gulp.start('styles');
    }, 2000);
  });
  gulp.watch(path.JS, function() {
    setTimeout(function () {
      gulp.start('scripts');
    }, 2000);
  });
});

gulp.task('img', function() {
  return gulp.src(path.IMG)
    .pipe(imagemin())
    .pipe(gulp.dest(path.DEST + '/img'))
});

gulp.task('styles', function() {
  return gulp.src(path.CSS)
    .pipe(sass({includePaths: ['./node_modules']}).on('error', sass.logError))
    .pipe(autoprefixer({ browsers: ['last 2 versions'] }))
    .pipe(cleanCSS({keepSpecialComments: '0'}))
		.pipe(concat('bundle.css'))
    .pipe(gulp.dest(path.DEST + '/css'))
});

gulp.task('scripts', function() {
  return gulp.src(path.JS)
  .pipe(browserify())
  .pipe(uglify())
  .pipe(concat('bundle.js'))
  .pipe(gulp.dest(path.DEST + '/js'))
});
