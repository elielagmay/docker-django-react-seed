import storage from '../store';

export const checkHttpStatus = (response) => {
    if (response.status >= 200 && response.status < 300) {
        return response;
    } else {
        var error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
};

export const parseJSON = (response) => {
    return response.json();
};

export const createResourceAction = (opts, sendType, doneType, failType) => {
    const rawUrl = opts.url;
    const method = opts.method || 'GET';

    const resourceSendAction = () => ({
      type: sendType,
    });

    const resourceDoneAction = (resource) => ({
        type: doneType,
        payload: resource,
    });

    const resourceFailAction = (error) => ({
        type: failType,
        payload: error,
    });

    return (data = {}) => (dispatch) => {
        dispatch(resourceSendAction());

        let url = rawUrl;
        let fetchOptions = {
            method: method,
            credentials: 'include',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
        };

        if (data.id) {
            url = url.replace(/:id/, data.id);
        }

        if (data.query) {
            url += '?';
            for (const key in data.query) {
                url += key + '=' + data.query[key] + '&';
            }
        }

        if (data.body) {
            fetchOptions.body = JSON.stringify(data.body);
        }

        const token = storage.get('AUTH_TOKEN');
        if (token) {
            fetchOptions.headers.Authorization = 'JWT ' + token;
        }

        return fetch(url, fetchOptions)
            .then(checkHttpStatus)
            .then(parseJSON)
            .then(resource => {
                setTimeout(function() {
                    dispatch(resourceDoneAction(resource));
                }, 50);
            })
            .catch(error => {
                dispatch(resourceFailAction(error));
            });
    };
};
