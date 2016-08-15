const storage = localStorage;

export const dataStorage = {
    get: (key) => {
        return storage.getItem(key);
    },
    set: (key, value) => {
        return storage.setItem(key, value);
    },
    unset: (key) => {
        return storage.removeItem(key);
    },
    clear: () => {
        return storage.clear();
    }
};
