type ClickCallback = (e: Event) => void;
type UserCallback = (...args: any[]) => void;

const subscribers = new Map<UserCallback, ClickCallback>();

export function addClickOutside(element: HTMLElement, callback: UserCallback) {
    let clickFunc = (e: Event) => {
        if (element && !element.contains(e.target as Node)) {
            callback();
        }
    }
    subscribers.set(callback, clickFunc);
    window.addEventListener('click', clickFunc);
}

export function removeClickOutside(callback: UserCallback) {
    let clickFunc = subscribers.get(callback);
    if (clickFunc) {
        window.removeEventListener('click', clickFunc);
        subscribers.delete(callback);
    } else {
        console.log("Didn't find func")
    }
}