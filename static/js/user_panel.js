document.addEventListener('DOMContentLoaded', function () {
    // Change profile photo functionality
    const changePhotoBtn = document.querySelector('.change-photo');
    changePhotoBtn.addEventListener('click', function () {
        // In a real app, this would open a file dialog
        alert('In a real application, this would open a file dialog to upload a new profile photo.');
    });

    // Notification bell functionality
    const notificationBell = document.querySelector('.notification-bell');
    notificationBell.addEventListener('click', function () {
        const count = document.querySelector('.notification-count');
        count.style.display = 'none';
        alert('Notifications cleared!');
    });

    // Edit profile button functionality
    const editBtn = document.querySelector('.edit-btn');
    editBtn.addEventListener('click', function () {
        alert('Edit profile form would appear here.');
    });

    // Responsive sidebar toggle (for mobile)
    // This would be implemented with a hamburger menu in a real mobile implementation
});

// In a real application, you would fetch user data from an API
async function fetchUserData() {
    try {
        // const response = await fetch('/api/user');
        // const data = await response.json();
        // populateDashboard(data);
        console.log('User data would be fetched from API in a real application');
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}

function populateDashboard(userData) {
    // This function would populate the dashboard with real user data
    // Example:
    // document.querySelector('.user-profile h3').textContent = userData.name;
    // document.querySelector('.user-profile p').textContent = userData.membership;
    // etc.
}

// Initialize the dashboard
fetchUserData();


document.addEventListener('DOMContentLoaded', function () {
    // Handle profile image upload
    const imageUpload = document.getElementById('imageUpload');
    const profileImage = document.getElementById('profileImage');

    if (imageUpload && profileImage) {
        imageUpload.addEventListener('change', function (e) {
            if (e.target.files && e.target.files[0]) {
                const reader = new FileReader();

                reader.onload = function (event) {
                    profileImage.src = event.target.result;
                }

                reader.readAsDataURL(e.target.files[0]);
            }
        });
    }

    // Handle form submission
    const profileForm = document.getElementById('profileForm');
    if (profileForm) {
        profileForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // In a real app, you would send this data to the server
            const formData = {
                name: document.getElementById('fullName').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                birthDate: document.getElementById('birthDate').value,
                gender: document.querySelector('input[name="gender"]:checked').value,
                address: document.getElementById('address').value,
                // Add image handling in a real app
            };

            console.log('Form data:', formData);
            alert('Profile updated successfully!');

            // Redirect back to dashboard after saving
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 1000);
        });
    }

    // Shared functionality (same as before)
    const changePhotoBtn = document.querySelector('.change-photo');
    if (changePhotoBtn) {
        changePhotoBtn.addEventListener('click', function () {
            alert('In a real application, this would open a file dialog to upload a new profile photo.');
        });
    }

    const notificationBell = document.querySelector('.notification-bell');
    if (notificationBell) {
        notificationBell.addEventListener('click', function () {
            const count = document.querySelector('.notification-count');
            count.style.display = 'none';
            alert('Notifications cleared!');
        });
    }
});

// In a real application, you would fetch user data from an API
async function fetchUserData() {
    try {
        // const response = await fetch('/api/user');
        // const data = await response.json();
        // populateDashboard(data);
        console.log('User data would be fetched from API in a real application');
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}

function populateDashboard(userData) {
    // This function would populate the dashboard with real user data
    // Example:
    // document.querySelector('.user-profile h3').textContent = userData.name;
    // document.querySelector('.user-profile p').textContent = userData.membership;
    // etc.
}

// Initialize the dashboard
fetchUserData();

document.addEventListener('DOMContentLoaded', function () {
    // Shared functionality for all pages

    // Handle active state in filter buttons
    const filterButtons = document.querySelectorAll('.filter-options button');
    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });


    // Handle wishlist item removal
    const removeButtons = document.querySelectorAll('.remove-btn');
    removeButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.stopPropagation();
            const item = this.closest('.wishlist-item');
            if (confirm('Are you sure you want to remove this item from your wishlist?')) {
                item.style.opacity = '0';
                setTimeout(() => {
                    item.remove();
                    // In real app, you would call API to remove from wishlist
                    updateWishlistCount(-1);
                }, 300);
            }
        });
    });

    // Handle add to cart from wishlist
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            // In real app, you would call API to add to cart
            alert('Item added to cart!');
        });
    });

    // Update wishlist count in sidebar
    function updateWishlistCount(change) {
        const wishlistCount = document.querySelector('.sidebar-nav a[href="wishlist.html"]');
        if (wishlistCount) {
            const currentText = wishlistCount.textContent;
            const match = currentText.match(/\((\d+)\)/);
            let count = match ? parseInt(match[1]) : 0;
            count += change;

            if (count > 0) {
                wishlistCount.innerHTML = wishlistCount.innerHTML.replace(/\(\d+\)|$/, $({count}));
            } else {
                wishlistCount.innerHTML = wishlistCount.innerHTML.replace(/\(\d+\)/, '');
            }
        }
    };

    // Profile image upload (from profile page)
    // const imageUpload = document.getElementById('imageUpload');
    // if (imageUpload) {
    //     imageUpload.addEventListener('change', function (e) {
    //         if (e.target.files && e.target.files[0]) {
    //             const reader = new FileReader();
    //             const profileImage = document.getElementById('profileImage') ||
    //                 document.querySelector('.profile-img');
    //
    //             reader.onload = function (event) {
    //                 if (profileImage) {
    //                     profileImage.src = event.target.result;
    //                     // Update image in sidebar too
    //                     const sidebarImage = document.querySelector('.sidebar .profile-img');
    //                     if (sidebarImage) sidebarImage.src = event.target.result;
    //                 }
    //             }
    //
    //             reader.readAsDataURL(e.target.files[0]);
    //         }
    //     });
    // }
});

// Initialize the dashboard
fetchUserData();

// async function fetchUserData() {
//     try {
//         // In a real app, you would fetch from API
//         console.log('Fetching user data...');
//
//         // Simulate API call
//         setTimeout(() => {
//             // Update all profile images
//             const profileImages = document.querySelectorAll('.profile-img, #profileImage');
//             profileImages.forEach(img => {
//                 img.src = 'https://randomuser.me/api/portraits/men/32.jpg';
//             });
//
//             // Update user name
//             const userNames = document.querySelectorAll('.user-profile h3, .user-menu span');
//             userNames.forEach(el => {
//                 el.textContent = 'John Doe';
//             });
//         }, 500);
//     } catch (error) {
//         console.error('Error fetching user data:', error);
//     }
// }

document.addEventListener('DOMContentLoaded', function () {
    // تغییر بین تب‌های تنظیمات
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(button => {
        button.addEventListener('click', function () {
            // حذف کلاس active از همه دکمه‌ها و تب‌ها
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabPanes.forEach(pane => pane.classList.remove('active'));

            // اضافه کردن کلاس active به دکمه و تب مربوطه
            this.classList.add('active');
            const tabId = this.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // کپی کردن کلید API
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', function () {
            const apiKey = this.previousElementSibling.textContent;
            navigator.clipboard.writeText(apiKey).then(() => {
                const originalText = this.textContent;
                this.textContent = 'کپی شد!';
                setTimeout(() => {
                    this.textContent = originalText;
                }, 2000);
            });
        });
    });

    // نمایش دیالوگ حذف حساب کاربری
    const deleteAccountBtn = document.querySelector('.delete-btn');
    if (deleteAccountBtn) {
        deleteAccountBtn.addEventListener('click', function () {
            if (confirm('آیا مطمئن هستید که می‌خواهید حساب کاربری خود را حذف کنید؟ این عمل غیرقابل بازگشت است.')) {
                alert('در یک برنامه واقعی، اینجا حساب کاربری حذف می‌شد.');
                // کد واقعی حذف حساب کاربری
                // await deleteUserAccount();
            }
        });
    }

    // نمایش دیالوگ خروج از همه دستگاه‌ها
    const logoutAllBtn = document.querySelector('.logout-btn');
    if (logoutAllBtn) {
        logoutAllBtn.addEventListener('click', function () {
            if (confirm('آیا می‌خواهید از همه دستگاه‌ها خارج شوید؟')) {
                alert('در یک برنامه واقعی، اینجا کاربر از همه دستگاه‌ها خارج می‌شد.');
                // کد واقعی خروج از همه دستگاه‌ها
                // await logoutAllDevices();
            }
        });
    }

    // نمایش دیالوگ افزودن روش پرداخت جدید
    const addPaymentBtn = document.querySelector('.add-payment-btn');
    if (addPaymentBtn) {
        addPaymentBtn.addEventListener('click', function () {
            alert('در یک برنامه واقعی، اینجا فرم افزودن کارت جدید نمایش داده می‌شد.');
        });
    }

    // نمایش دیالوگ حذف روش پرداخت
    const removePaymentBtns = document.querySelectorAll('.remove-btn');
    removePaymentBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            if (confirm('آیا مطمئن هستید که می‌خواهید این روش پرداخت را حذف کنید؟')) {
                const paymentCard = this.closest('.payment-card');
                paymentCard.style.opacity = '0';
                setTimeout(() => {
                    paymentCard.remove();
                }, 300);
            }
        });
    });

    // ذخیره تنظیمات
    // const settingsForms = document.querySelectorAll('.settings-form');
    // settingsForms.forEach(form => {
    //     form.addEventListener('submit', function (e) {
    //         e.preventDefault();
    //         alert('تنظیمات با موفقیت ذخیره شد.');
    //         // در یک برنامه واقعی، اینجا داده‌ها به سرور ارسال می‌شد
    //         // await saveSettings();
    //     });
    // });
});

// Settings Tab Functionality
const tabButtons = document.querySelectorAll('.tab-btn');
const tabPanes = document.querySelectorAll('.tab-pane');

tabButtons.forEach(button => {
    button.addEventListener('click', function () {
        // Remove active class from all buttons and panes
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabPanes.forEach(pane => pane.classList.remove('active'));

        // Add active class to clicked button and corresponding pane
        this.classList.add('active');
        const tabId = this.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});

// Copy API Key Functionality
const copyButtons = document.querySelectorAll('.copy-btn');
copyButtons.forEach(button => {
    button.addEventListener('click', function () {
        const apiKey = this.previousElementSibling.textContent;
        navigator.clipboard.writeText(apiKey).then(() => {
            const originalText = this.textContent;
            this.textContent = 'Copied!';
            setTimeout(() => {
                this.textContent = originalText;
            }, 2000);
        });
    });
});

// Delete Account Confirmation
const deleteAccountBtn = document.querySelector('.delete-btn');
if (deleteAccountBtn) {
    deleteAccountBtn.addEventListener('click', function () {
        if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
            alert('In a real application, your account would be deleted now.');
            // Actual account deletion code would go here
        }
    });
}

// Logout All Devices Confirmation
const logoutAllBtn = document.querySelector('.logout-btn');
if (logoutAllBtn) {
    logoutAllBtn.addEventListener('click', function () {
        if (confirm('Are you sure you want to logout from all devices?')) {
            alert('In a real application, you would be logged out from all devices.');
            // Actual logout all code would go here
        }
    });
}

// Form Submissions
// const settingsForms = document.querySelectorAll('.settings-form');
// settingsForms.forEach(form => {
//     form.addEventListener('submit', function (e) {
//         e.preventDefault();
//         alert('Settings saved successfully!');
//         // Actual save functionality would go here
//     });
// });


document.addEventListener('DOMContentLoaded', function () {
    // Payment Method Modal
    const addPaymentBtn = document.getElementById('addPaymentBtn');
    const paymentModal = document.getElementById('paymentModal');
    const closeBtn = document.querySelector('.close-btn');
    const cancelBtn = document.querySelector('.cancel-btn');

    // Show modal when Add Payment button is clicked
    if (addPaymentBtn) {
        addPaymentBtn.addEventListener('click', function () {
            paymentModal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        });
    }

    // Close modal when X button is clicked
    if (closeBtn) {
        closeBtn.addEventListener('click', function () {
            paymentModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    }

    // Close modal when Cancel button is clicked
    if (cancelBtn) {
        cancelBtn.addEventListener('click', function () {
            paymentModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    }

    // Close modal when clicking outside the modal content
    paymentModal.addEventListener('click', function (e) {
        if (e.target === paymentModal) {
            paymentModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Form submission
    const paymentForm = document.getElementById('paymentForm');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // In a real app, you would validate and process the payment method
            alert('Payment method added successfully!');

            // Close the modal
            paymentModal.style.display = 'none';
            document.body.style.overflow = 'auto';

            // Reset the form
            paymentForm.reset();
        });
    }

    // Remove payment method
    const removeBtns = document.querySelectorAll('.remove-btn');
    removeBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            if (confirm('Are you sure you want to remove this payment method?')) {
                const paymentCard = this.closest('.payment-method-card');
                paymentCard.style.opacity = '0';
                setTimeout(() => {
                    paymentCard.remove();
                }, 300);
            }
        });
    });

    // Set default payment method
    const setDefaultBtns = document.querySelectorAll('.set-default-btn:not(:disabled)');
    setDefaultBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            // Remove default class from all cards
            document.querySelectorAll('.payment-method-card').forEach(card => {
                card.classList.remove('default');
            });

            // Add default class to current card
            const paymentCard = this.closest('.payment-method-card');
            paymentCard.classList.add('default');

            // Disable set as default button on this card
            this.disabled = true;

            // Enable set as default buttons on other cards
            setDefaultBtns.forEach(otherBtn => {
                if (otherBtn !== this) {
                    otherBtn.disabled = false;
                }
            });

            alert('Default payment method updated!');
        });
    });

    // Format card number input
    const cardNumberInput = document.getElementById('cardNumber');
    if (cardNumberInput) {
        cardNumberInput.addEventListener('input', function (e) {
            let value = this.value.replace(/\s+/g, '');
            if (value.length > 0) {
                value = value.match(new RegExp('.{1,4}', 'g')).join(' ');
            }
            this.value = value;
        });
    }

    // Format expiry date input
    const expiryDateInput = document.getElementById('expiryDate');
    if (expiryDateInput) {
        expiryDateInput.addEventListener('input', function (e) {
            let value = this.value.replace(/\D/g, '');
            if (value.length > 2) {
                value = value.substring(0, 2) + '/' + value.substring(2, 4);
            }
            this.value = value;
        });
    }
});