// Hero Text Animation
function homeHeroAnimator() {
    // Create variables
    let mainWrapper = document.getElementById("hero-anim");
    let elementsWrapper = mainWrapper.querySelectorAll(".h-hero-header-highlight");
    let firstElement = elementsWrapper[0];
    let secondElement = elementsWrapper[1];
    let firstItems = firstElement.querySelectorAll(".hero-highlight-wrapper");
    let secondItems = secondElement.querySelectorAll(".hero-highlight-wrapper");
    let tl;
    let throttle;
    let progress = 0;
    // Function for setting base values
    function setBase(ele) {
        ele.forEach((e) => {
            e.style.display = "none";
            e.style.width = "0";
        });
        ele[0].style.display = "block";
        ele[0].style.width = "auto";
    }

    function animation() {
        // Set base values
        setBase(firstItems);
        setBase(secondItems);
        // Establish timeline
        tl = gsap.timeline({
            repeat: -1
        });
        // Animate first tl
        for (let item = 0; item < firstItems.length; item++) {
            if (item == 0) {
                tl.add(gsap.to(firstItems[item], {
                    width: 0,
                    duration: 0.6
                }), 1);
                tl.add(gsap.set(firstItems[item], {
                    display: "none"
                }), ">");
            } else if ((item != firstItems.length - 1) && (item != 0)) {
                tl.add(gsap.set(firstItems[item], {
                    display: "block"
                }), ">");
                tl.add(gsap.to(firstItems[item], {
                    width: "auto",
                    duration: 0.6
                }), ">");
                tl.add(gsap.to(firstItems[item], {
                    width: 0,
                    duration: 0.6
                }), ">2.6");
                tl.add(gsap.set(firstItems[item], {
                    display: "none"
                }), ">");
            } else {
                tl.add(gsap.set(firstItems[item], {
                    display: "block"
                }), ">");
                tl.add(gsap.to(firstItems[item], {
                    width: "auto",
                    duration: 0.6
                }), ">");
                tl.add(gsap.to(firstItems[item], {
                    width: 0,
                    duration: 0.6
                }), ">2.6");
                tl.add(gsap.set(firstItems[0], {
                    display: "block"
                }), ">");
                tl.add(gsap.to(firstItems[0], {
                    width: "auto",
                    duration: 0.6
                }), ">");
            }
        }
        // Animate second tl
        for (let item = 0; item < secondItems.length; item++) {
            if (item == 0) {
                tl.add(gsap.to(secondItems[item], {
                    width: 0,
                    duration: 0.6
                }), 2.6);
                tl.add(gsap.set(secondItems[item], {
                    display: "none"
                }), ">");
            } else if ((item != secondItems.length - 1) && (item != 0)) {
                tl.add(gsap.set(secondItems[item], {
                    display: "block"
                }), ">");
                tl.add(gsap.to(secondItems[item], {
                    width: "auto",
                    duration: 0.6
                }), ">");
                tl.add(gsap.to(secondItems[item], {
                    width: 0,
                    duration: 0.6
                }), ">2.6");
                tl.add(gsap.set(secondItems[item], {
                    display: "none"
                }), ">");
            } else {
                tl.add(gsap.set(secondItems[item], {
                    display: "block"
                }), ">");
                tl.add(gsap.to(secondItems[item], {
                    width: "auto",
                    duration: 0.6
                }), ">");
                tl.add(gsap.to(secondItems[item], {
                    width: 0,
                    duration: 0.6
                }), ">2.6");
                tl.add(gsap.set(secondItems[0], {
                    display: "block"
                }), ">");
                tl.add(gsap.to(secondItems[0], {
                    width: "auto",
                    duration: 0.6
                }), ">");
            }
        }
        tl.progress(progress)
    }
    animation();
    // Restart animation on window resize
    function restartTL() {
        progress = tl.progress();
        tl.kill();
        animation();
    };
    window.addEventListener("resize", function() {
        clearTimeout(throttle);
        tl.pause();
        throttle = this.setTimeout(restartTL, 500);
    });
}
homeHeroAnimator();
// Portfolio into view
function portfolioAnimation() {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".swiper.swiper-portfolio",
            start: "top 60%",
        }
    });
    tl.from(".portfolio-item", {
        y: "5%",
        opacity: 0,
        stagger: {
            each: 0.3,
            from: "start"
        },
        ease: "power1.in",
        duration: 0.5
    });
}
portfolioAnimation();
// Testimonials into view
function testimonialAnimation() {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".swiper.swiper-testimonials",
            start: "top 70%",
        }
    });
    tl.from(".testimonial-item", {
        y: "5%",
        opacity: 0,
        stagger: {
            each: 0.3,
            from: "start"
        },
        ease: "power1.in",
        duration: 0.5
    });
}
testimonialAnimation();
// Service into view
function serviceAnimation1() {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".service-row.service-row-1",
            start: "top 70%",
        }
    });
    tl.from(".service-item.service-row-1", {
        y: "5%",
        opacity: 0,
        stagger: {
            each: 0.3,
            from: "start"
        },
        ease: "power1.in",
        duration: 0.5
    });
}
serviceAnimation1();

function serviceAnimation2() {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".service-row.service-row-2",
            start: "top 70%",
        }
    });
    tl.from(".service-item.service-row-2", {
        y: "5%",
        opacity: 0,
        stagger: {
            each: 0.3,
            from: "start"
        },
        ease: "power1.in",
        duration: 0.5
    });
}
serviceAnimation2();
// Team into view
function teamAnimation() {
    let tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".h-about-team",
            start: "top 70%",
        }
    });
    tl.from(".team-member", {
        y: "5%",
        opacity: 0,
        stagger: {
            each: 0.2,
            from: "start"
        },
        ease: "power1.in",
        duration: 0.4
    });
}
teamAnimation();
var mySwiper = new Swiper('.swiper-portfolio', {
    // Optional parameters
    slidesPerView: 1,
    spaceBetween: 30,
    loop: false,
    speed: 800,
    centeredSlides: false,
    lazy: true,
    navigation: {
        nextEl: '.swiper-arrow-next',
        prevEl: '.swiper-arrow-previous',
        disabledClass: 'swiper-arrow-disabled',
    },
    keyboard: {
        enabled: true,
    },
    breakpoints: {
        0: {
            /* Webflow - mobile portrait */
            slidesPerView: 1.1,
            spaceBetween: 12,
            centeredSlides: false,
        },
        478: {
            /* Webflow - mobile landscape */
            slidesPerView: 2,
            spaceBetween: 24,
        },
        767: {
            /* Webflow - tablet */
            slidesPerView: 2,
            spaceBetween: 24,
        },
        988: {
            /* Webflow - desktop */
            slidesPerView: 2,
            spaceBetween: 40,
        },
    },
})
var mySwiper = new Swiper('.swiper-testimonials', {
    // Optional parameters
    slidesPerView: 1,
    spaceBetween: 30,
    loop: false,
    speed: 800,
    centeredSlides: false,
    lazy: true,
    navigation: {
        nextEl: '.swiper-arrow-next',
        prevEl: '.swiper-arrow-previous',
        disabledClass: 'swiper-arrow-disabled',
    },
    keyboard: {
        enabled: true,
    },
    breakpoints: {
        0: {
            /* Webflow - mobile portrait */
            slidesPerView: 1.1,
            spaceBetween: 12,
            centeredSlides: false,
        },
        478: {
            /* Webflow - mobile landscape */
            slidesPerView: 2,
            spaceBetween: 24,
        },
        767: {
            /* Webflow - tablet */
            slidesPerView: 2,
            spaceBetween: 24,
        },
        988: {
            /* Webflow - desktop */
            slidesPerView: 2.5,
            spaceBetween: 40,
        },
    },
})