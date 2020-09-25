jQuery(document).ready(function($) {
    "use strict";
    /* Menu */
    $(".js-hidden-menu").hide();
    $(".js-nav-menu").on("click", function() {
        $(this).toggleClass('open');
        $(this).next().toggleClass('active');

    });
    $(".navbar-toggle").on("click", function() {
        $(".js-dropdown-menu").removeClass('active');

    });
    //tabs checkout page 2
    $("ul.tabs").each(function() {
        $(this).children().first().addClass("active");
        $(this).next().children().first().show().addClass("active");
    });
    $("ul.tabs li").each(function() {
        $(this).on("click", function() {
            var tab_content = $(this).parent().next().children();
            $(this).parent().children().removeClass("active");
            $(this).addClass("active");
            tab_content.hide().removeClass("active");
            var activeTab = $(this).attr("rel");
            $("#" + activeTab).fadeIn(400).addClass("active");
        });
    });

    function toggleMenu() {
        
        if ($(window).width() < 769) {
            //initially hide navigation
            $(".js-dropdown-menu").removeClass('active');
            $(document).on("click", function(e){
                 
                var p = $(e.target).closest('.navbar-default').length
                if (!p) {
                    $(".js-dropdown-menu").removeClass('active');
                }
            });

        } else $(".js-dropdown-open").show();
    };

    //call function on load and page resize
    $(window).load(toggleMenu);
    $(window).resize(toggleMenu);

    //menu change icon and dropdown
    $(".js-menubar li .js-plus-icon").on("click", function() {
        $(this).toggleClass('minus');
        $(this).parent().find(".dropdown-menu").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });
    //OPEN MENU HOMEPAGE 6
    //// =========== OPEN MENU ==================//
    $(".js-navbar-wrapper .js-navbar-button .js-bars ").on("click", function(e) {
        $(".js-navbar-wrapper #bars").toggleClass("open");
        e.stopPropagation();
    });

    $(document).on("mouseup", function(e) {
        
        var container = $(".js-navbar-wrapper #bars,.js-navbar-wrapper .js-navbar-button .js-bars ");

        if (!container.is(e.target) // if the target of the click isn't the container...
            &&
            container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            $('.js-navbar-wrapper #bars').removeClass('open');
        }
    });
    // =========== OPEN CART ==================//
    $(".js-navbar-wrapper .js-navbar-meta .js-cart").on("click", function(e) {
        $(".js-navbar-wrapper #cart").toggleClass('open');
        e.stopPropagation();
    });
   $(document).on("mouseup", function(e) {
        
        var container = $(".js-navbar-wrapper #cart,.js-navbar-wrapper .js-navbar-button .js-cart ");

        if (!container.is(e.target) // if the target of the click isn't the container...
            &&
            container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            $('.js-navbar-wrapper #cart').removeClass('open');
        }
    });
    //SHOP LISTING FILTER
    // ======== ADD CLASS ACTIVE 
    $(".filter-cate ul li").on("click", function() {
        $('li.active').removeClass('active');
        $(this).addClass('active');
    });
    //SHOP GRID
    $(".button-view .col").on("click", function() {
        $(this).toggleClass('active');
        $(".product-list").removeClass("list-item");
        $(".button-view .list").removeClass("active");
    });
    $(".button-view .list").on("click", function() {
        $(this).toggleClass("active");
        $(".product-list").addClass("list-item");
        $(".button-view .col").removeClass("active");
    });
    // SHOPPING CART Quantity increment buttons
    
    var quantitiy = 0;
    $('.quantity-right-plus').on("click", function(e) {

        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#quantity').val(),10);

        // If is not undefined

        $('#quantity').val(quantity + 1);


        // Increment    
    });

    $('.quantity-left-minus').on("click", function(e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#quantity').val(),10);

        // If is not undefined

        // Increment
        if (quantity > 0) {
            $('#quantity').val(quantity - 1);
        }
    });

    // Price Slider
    if ($('.price-slider').length > 0) {
        $('.price-slider').slider({
            min: 100,
            max: 700,
            step: 10,
            value: [100, 400],


        });
    }

    // brand carousel
    $('.js-owl-brand').owlCarousel({
        loop: true,
        nav: true,
        navText: ["", ""],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    })
    // js multiple image PRODUCT SINGLE
    $('.multiple-img-list').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.main-img',
        dots: false,
        arrows: false,
        focusOnSelect: true,

    });
    $('.main-img').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.multiple-img-list'
    });
    $('.portfolio-thumb-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.portfolio-item-slider',
        dots: false,
        arrows: false,
        focusOnSelect: true
    });
    $('.portfolio-thumb-slider').on('afterChange', function(event, slick, currentSlide, nextSlide) {
    
        //remove all active class
        $('.portfolio-thumb-slider .slick-slide').removeClass('slick-current');
        //set active class for current slide
        $('.portfolio-thumb-slider .slick-slide:not(.slick-cloned)').eq(currentSlide).addClass('slick-current');
    });

    $('.portfolio-item-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.portfolio-thumb-slider'
    });

    $('.portfolio-thumb-slider .slick-slide:not(.slick-cloned)').eq(0).addClass('slick-current');

    $('.slick-slider-wrapper').css('opacity', '1');

    // banner carousel
    $('.js-banner').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
    });
    // product carousel
    $('.js-owl-product').owlCarousel({
        margin: 15,
        autoplay: true,
        autoplayTimeout: 3000,
        loop: true,
        nav: false,
        navText: ["", ""],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    })
    // COUNTDOWN 
    $.fn.ENGO_CountDown = function(options) {
        return this.each(function() {
            // get instance of the ENGO_CountDown.
            new $.ENGO_CountDown(this, options);
        });
    }
    $.ENGO_CountDown = function(obj, options) {
        var ddiff, gsecs;
        this.options = $.extend({
            autoStart: true,
            LeadingZero: true,
            DisplayFormat: "<div><span>%%D%%</span> Days</div><div><span>%%H%%</span> Hours</div><div><span>%%M%%</span> Mins</div><div><span>%%S%%</span> Secs</div>",
            FinishMessage: "Expired",
            CountActive: true,
            TargetDate: null
        }, options || {});
        if (this.options.TargetDate == null || this.options.TargetDate == '') {
            return;
        }
        this.timer = null;
        this.element = obj;
        this.CountStepper = -1;
        this.CountStepper = Math.ceil(this.CountStepper);
        this.SetTimeOutPeriod = (Math.abs(this.CountStepper) - 1) * 1000 + 990;
        var dthen = new Date(this.options.TargetDate);
        var dnow = new Date();
        if (this.CountStepper > 0) {
            ddiff = new Date(dnow - dthen);
        } else {
            ddiff = new Date(dthen - dnow);
        }
        gsecs = Math.floor(ddiff.valueOf() / 1000);
        this.CountBack(gsecs, this);
    };
    $.ENGO_CountDown.fn = $.ENGO_CountDown.prototype;
    $.ENGO_CountDown.fn.extend = $.ENGO_CountDown.extend = $.extend;
    $.ENGO_CountDown.fn.extend({
        calculateDate: function(secs, num1, num2) {
            var s = ((Math.floor(secs / num1)) % num2).toString();
            if (this.options.LeadingZero && s.length < 2) {
                s = "0" + s;
            }
            return "<b>" + s + "</b>";
        },
        CountBack: function(secs, self) {
            var DisplayStr;
            if (secs < 0) {
                self.element.innerHTML = '<div class="labelexpired"> ' + self.options.FinishMessage + "</div>";
                return;
            }
            clearInterval(self.timer);
            DisplayStr = self.options.DisplayFormat.replace(/%%D%%/g, self.calculateDate(secs, 86400, 100000));
            DisplayStr = DisplayStr.replace(/%%H%%/g, self.calculateDate(secs, 3600, 24));
            DisplayStr = DisplayStr.replace(/%%M%%/g, self.calculateDate(secs, 60, 60));
            DisplayStr = DisplayStr.replace(/%%S%%/g, self.calculateDate(secs, 1, 60));
            self.element.innerHTML = DisplayStr;
            if (self.options.CountActive) {
                self.timer = null;
                self.timer = setTimeout(function() {
                    self.CountBack((secs + self.CountStepper), self);
                }, (self.SetTimeOutPeriod));
            }
        }

    });

    function init_countdown() {
        /** Countdown **/
        $('[data-countdown="countdown"]').each(function(index, el) {
            var $this = $(this);
            var $date = $this.data('date').split("-");
            $this.ENGO_CountDown({
                TargetDate: $date[0] + "/" + $date[1] + "/" + $date[2] + " " + $date[3] + ":" + $date[4] + ":" + $date[5],
                DisplayFormat: "<ul><li><span>%%D%% </span>days</li><li><span>%%H%% </span>hours</li><li><span>%%M%% </span>mins</li><li><span>%%S%%</span>secs</li></ul>",
                FinishMessage: "Expired"
            });
        });

    }
    init_countdown();

    function init_countdown2() {
        /** Countdown **/
        $('[data-countdown="countdownver2"]').each(function(index, el) {
            var $this = $(this);
            var $date = $this.data('date').split("-");
            $this.ENGO_CountDown({
                TargetDate: $date[0] + "/" + $date[1] + "/" + $date[2] + " " + $date[3] + ":" + $date[4] + ":" + $date[5],
                DisplayFormat: "<ul><li><span>%%H%% </span>Hrs</li><li><span>%%M%% </span>Mins</li><li><span>%%S%%</span>Secs</li></ul>",
                FinishMessage: "Expired"
            });
        });

    }
    init_countdown2();
});