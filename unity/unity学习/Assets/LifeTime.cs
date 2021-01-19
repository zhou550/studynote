using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LifeTime : MonoBehaviour {

	// Use this for initialization
	void Start () {
        Debug.Log("Start");
    }
	
	// Update is called once per frame
	void Update () {
        Debug.Log("Update");
    }
     void Awake()
    {
        Debug.Log("Awake");
    }
    void FixedUpdate()
    {
        Debug.Log("FixedUpdate");
    }
    private void LateUpdate()
    {
        Debug.Log("LateUpdate");
    }

}
