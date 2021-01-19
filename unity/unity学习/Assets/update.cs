using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class update : MonoBehaviour {

    private void FixedUpdate()
    {
        Debug.Log("===========FixedUpdate=======:  " + Time.deltaTime);
    }

    // Update is called once per frame
    void Update () {
        Debug.Log("==========Update========:  " + Time.deltaTime);
    }
}
