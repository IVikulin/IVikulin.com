// jQuery import
global.$ = global.jQuery = require('jquery');

// Fullpage and dependencies import
global.IScroll = require('fullpage.js/vendors/scrolloverflow');
require('fullpage.js');


// Fullpage initialization
$(document).ready(function() {
    $('#fullpage').fullpage({
        // Navigation
        menu: '#menu',
        lockAnchors: false,
        anchors:['about', 'works', 'contacts'],
        slidesNavigation: true,
        slidesNavPosition: 'bottom',

        // Scrolling
        css3: true,
        scrollingSpeed: 700,
        autoScrolling: true,
        fitToSection: true,
        fitToSectionDelay: 1000,
        scrollBar: false,
        easing: 'easeInOutCubic',
        easingcss3: 'ease',
        loopBottom: false,
        loopTop: false,
        loopHorizontal: true,
        continuousVertical: false,
        continuousHorizontal: false,
        scrollHorizontally: false,
        interlockedSlides: false,
        dragAndMove: false,
        offsetSections: false,
        resetSliders: false,
        fadingEffect: false,
        scrollOverflow: true,
        touchSensitivity: 15,
        normalScrollElementTouchThreshold: 5,

        // Accessibility
        keyboardScrolling: true,
        animateAnchor: true,
        recordHistory: true,

        // Design
        controlArrows: true,
        verticalCentered: true,
        paddingTop: '4rem',
        paddingBottom: '2rem',
        responsiveWidth: 0,
        responsiveHeight: 0
    });
});


// Preloader hiding
$(window).on("load", function() {
  $('#preloader').fadeOut();

  // Clear the task of forsed hiding, see base.html
  clearTimeout(loader_hiding);
});